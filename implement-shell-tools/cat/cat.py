import sys
import argparse


parser = argparse.ArgumentParser(
  prog = "concatenate-and-print-files",
  description = "The cat utility reads files sequentially, writing them to the standard output."
)

parser.add_argument("path", help = "The file to read and print", nargs = "+")

args = parser.parse_args()


def readAndPrintFile():
  buffer = []
  for path in args.path:
    buffer.append(readFile(path))
  printBuffer(buffer)

def readFile(path):
  try:
    with open(path, "r") as file:
      content = file.read()
    return content.strip().split("\n")
  except:
    return  ["cat.py: " + path + ": No such file or directory"]
  
def printBuffer(buffer):
  for fileContent in buffer:
    printContent(fileContent)

def printContent(fileContent):
  for string in fileContent:
    if string.startswith("cat.py:"):
      print(string, file = sys.stderr)
    else:
      print(string)

readAndPrintFile()