import sys
import argparse


parser = argparse.ArgumentParser(
  prog = "concatenate-and-print-files",
  description = "The cat utility reads files sequentially, writing them to the standard output."
)

parser.add_argument("path", help = "The file to read and print", nargs = "*")
parser.add_argument("-b", action = "store_true", help = "Number the non-blank output lines, starting at 1.")
parser.add_argument("-n", action = "store_true", help = "Number the output lines, starting at 1.")

args = parser.parse_args()

def start():
  if (args.path):
    readAndPrintFile()
  else:
    try:
      while (True):
        string = input()
        print(string)
    except EOFError:
      pass
    except KeyboardInterrupt:
      pass

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
    return  [f"cat.py: {path}: No such file or directory"]
  
def printBuffer(buffer):
  for fileContent in buffer:
    printContent(fileContent)

def printContent(fileContent):
  if fileContent[0].startswith("cat.py:"):
      print(fileContent[0], file = sys.stderr)
  elif (args.b):
    printWithFlagB(fileContent)
  elif(args.n):
    printWithFlagN(fileContent)
  else:
    printWithoutFlags(fileContent)

def printWithFlagB(fileContent):
  n = 1
  for string in fileContent:
    if (not string):
      print(string)
    else:
      print(str(n).rjust(6) + " " + string)
      n += 1

def printWithFlagN(fileContent):
  n = 1
  for string in fileContent:
    print(str(n).rjust(6) + " " + string)
    n += 1

def printWithoutFlags(fileContent):
  for string in fileContent:
    print(string)

start()
