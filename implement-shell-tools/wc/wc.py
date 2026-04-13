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

parser.add_argument("path", help = "path to file.", nargs = "*")
parser.add_argument("-l", action = "store_true", help = "The number of lines in each input file is written to the standard output.")
parser.add_argument("-w", action = "store_true", help = "The number of words in each input file is written to the standard output.")
parser.add_argument("-c", action = "store_true", help = "The number of characters in each input file is written to the standard output.")

args = parser.parse_args()


def start():
  data = collectData()
  output = formatOutput(data)
  printOutput(output)

def collectData():
  data = []
  if not len(args.path):
    content = sys.stdin.read()
    data.append(collectFileData({}, content))
  else:
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
    if (datum.get('s') == "d"):
      errors.append(f"{ERROR_PREFIX} {datum.get('p')}: Is a directory")
    elif (datum.get('s') == "f"):
      files.append(formatFileOutput(datum))
    else:
      errors.append(f"{ERROR_PREFIX} {datum.get('p')}: open: No such file or directory")

  if (len(data) > 1):
    files.append(formatTotalOutput(data))
  
  return errors + files

def formatFileOutput(datum):
  result = ""
  if (not args.l and not args.w and not args.c):
    result = f"{formatOutputNumber(datum.get('l'))}{formatOutputNumber(datum.get('w'))}{formatOutputNumber(datum.get('c'))}"
  else:
    if (args.l):
      result = f"{result}{formatOutputNumber(datum.get('l'))}"
    if (args.w):
      result = f"{result}{formatOutputNumber(datum.get('w'))}"
    if (args.c):
      result = f"{result}{formatOutputNumber(datum.get('c'))}"

  if (datum.get('p')):
    result = f"{result} {datum['p']}"
  
  return result

def formatTotalOutput(data):
  total = {"s": "t", "l": 0, "w": 0, "c": 0, "p": TOTAL_PATH};
  
  for datum in data:
    if (datum.get('s') == "f"):
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
