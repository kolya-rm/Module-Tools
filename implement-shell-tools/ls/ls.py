import os
import sys
import argparse

TERMINAL_LENGTH = 120

parser = argparse.ArgumentParser(
  prog = "list-directory-content",
  description = "For each operand that names a file of a type other than directory, ls displays its name as well as any requested, associated" \
    "information.  For each operand that names a file of type directory, ls displays the names of files contained within that directory, " \
    "as well as any requested, associated information."
)

parser.add_argument("path", help = "path to entries to list", nargs = "*")
parser.add_argument("-a", action = "store_true", help = "Include directory entries whose names begin with a dot (‘.’).")
parser.add_argument("-1", action = "store_true", help = "(The numeric digit “one”.) Force output to be one entry per line.")
args = parser.parse_args()


def start():
  output = []
  files = []
  directories = []

  checkInput(output, files, directories)
  if (len(files)):
    output.append(formatFilesOutput(files))
  formatDirectoriesOutput(output, directories, len(files))
  printOutput(output)

def checkInput(output, files, directories):
  if (not len(args.path)):
    directories.append(".")
    return
  
  for path in args.path:
    if (os.path.isdir(path)):
      directories.append(path)
    elif (os.path.isfile(path)):
      files.append(path)
    else:
      output.append(f"ls.py:  {path}: No such file ore directory")

  files.sort()
  directories.sort()

def formatFilesOutput(files):
  if (vars(args)["1"]):
    return "\n".join(files)
  maxLength = 0
  for name in files:
    if (maxLength < len(name)):
      maxLength = len(name)
  
  padLength = 0
  while (padLength < maxLength):
    padLength += 8

  output = ""
  lineLength = 0
  for name in files:
    output += name.ljust(padLength)
    lineLength += padLength
    if (TERMINAL_LENGTH - lineLength < padLength):
      output += "\n"
      lineLength = 0
  
  return output

def formatDirectoriesOutput(output, directories, isFilesExist):
  isSingleDirectory = len(directories) == 1
  for i in range(0, len(directories)):
    files = os.listdir(directories[i])
    if (args.a):
      files +=[".",".."]
    else:
      files = [file for file in files if not file.startswith(".")]
    files.sort()

    directoryOutput = formatFilesOutput(files)
    if (isFilesExist or not isSingleDirectory):
      directoryOutput = f"{directories[i]}:\n{directoryOutput}"
    if (isFilesExist or (not isSingleDirectory and i)):
      directoryOutput = f"\n{directoryOutput}"
    
    output.append(directoryOutput)

def printOutput(output):
  for string in output:
    if (string.startswith("ls.py:")):
      print(string, file = sys.stderr)
    else:
      print(string)


start()
