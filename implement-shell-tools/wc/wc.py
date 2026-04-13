import os
import sys
import argparse

parser = argparse.ArgumentParser(
  prog = "word-count",
  description = "word, line, and character count"
)

parser.add_argument("path", help = "", nargs = "+")

args = parser.parse_args()


def start():
  data = collectData()
  print(data)
  
def collectData():
  data = []
  
  for path in args.path:
    datum = {}
    if (os.path.isdir(path)):
      datum["s"] = "d"
    elif (os.path.isfile(path)):
      with open(path, "r") as file: 
        content = file.read()
      collectFileData(datum, content)
    else:
      datum["s"] = "e"
    datum["p"] = path
    data.append(datum)

  return data

def collectFileData(datum, content):
  datum["s"] = "f"
  datum["l"] = content.count("\n")
  datum["w"] = len(content.strip().split())
  datum["c"] = len(content)

  return datum

start()
