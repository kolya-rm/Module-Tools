import os
import sys
import argparse

NUMBER_PADDING = 8
ERROR_PREFIX = "wc.mjs:"
TOTAL_PATH = "total"


parser = argparse.ArgumentParser(
  prog = "word-count",
  description = "word, line, and character count"
)

parser.add_argument("path", help = "", nargs = "+")

args = parser.parse_args()


def start():
  data = collectData()
  output = formatOutput(data)
  printOutput(output)

def collectData():
  data = []
  
  for path in args.path:
    datum = {}
    if (os.path.isdir(path)):
      datum['s'] = "d"
    elif (os.path.isfile(path)):
      with open(path, "r") as file: 
        content = file.read()
      collectFileData(datum, content)
    else:
      datum['s'] = "e"
    datum['p'] = path
    data.append(datum)

  return data

def collectFileData(datum, content):
  datum['s'] = "f"
  datum['l'] = content.count("\n")
  datum['w'] = len(content.strip().split())
  datum['c'] = len(content)

  return datum

def formatOutput(data):
  errors = []
  files = []

  for datum in data:
    if (datum['s'] == "d"):
      errors.append(f"{ERROR_PREFIX} {datum['p']}: Is a directory")
    elif (datum['s'] == "f"):
      files.append(formatFileOutput(datum))
    else:
      errors.append(f"{ERROR_PREFIX} {datum['p']}: open: No such file or directory")

  if (len(data) > 1):
    files.append(formatTotalOutput(data))
  
  return errors + files

def formatFileOutput(datum):
  result = f"{formatOutputNumber(datum['l'])}{formatOutputNumber(datum['w'])}{formatOutputNumber(datum['c'])}"

  if (datum["p"]):
    result = f"{result} {datum['p']}"
  
  return result

def formatTotalOutput(data):
  total = {"s": "t", "l": 0, "w": 0, "c": 0, "p": TOTAL_PATH};
  
  for datum in data:
    if (datum['s'] == "f"):
      total['l'] += datum['l']
      total['w'] += datum['w']
      total['c'] += datum['c']
  
  return formatFileOutput(total)

def formatOutputNumber(number):
  return str(number).rjust(NUMBER_PADDING)

def printOutput(output):
  for string in output:
    if (string.startswith(ERROR_PREFIX)):
      print(string, file = sys.stderr)
    else:
      print(string)

start()
