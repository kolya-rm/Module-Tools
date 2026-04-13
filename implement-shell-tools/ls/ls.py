import os
import argparse

parser = argparse.ArgumentParser(
  prog = "list-directory-content",
  description = "For each operand that names a file of a type other than directory, ls displays its name as well as any requested, associated" \
    "information.  For each operand that names a file of type directory, ls displays the names of files contained within that directory, " \
    "as well as any requested, associated information."
)

parser.add_argument("path", help = "path to entries to list", nargs = "+")
args = parser.parse_args()


def start():
  output = []
  files = []
  directories = []

  checkInput(output, files, directories)

  print(output)
  print(files)
  print(directories)

def checkInput(output, files, directories):
  for path in args.path:
    if (os.path.isdir(path)):
      directories.append(path)
    elif (os.path.isfile(path)):
      files.append(path)
    else:
      output.append(f"ls.py:  {path}: No such file ore directory")

  files.sort()
  directories.sort()

start()