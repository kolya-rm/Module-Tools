import argparse

parser = argparse.ArgumentParser(
  prog = "concatenate-and-print-files",
  description = "The cat utility reads files sequentially, writing them to the standard output."
)

parser.add_argument("path", help = "The file to read and print")

args = parser.parse_args()

def readAndPrintFile():
  buffer = []
  buffer += readFile(args.path)
  printBuffer(buffer)

def readFile(path):
  try:
    with open(path, "r") as file:
      content = file.read()
    return content.strip().split("\n")
  except:
    return  ["cat.js: " + path + ": No such file or directory"]
  
def printBuffer(buffer):
  for content in buffer:
    print(content)

readAndPrintFile()