import argparse

parser = argparse.ArgumentParser(
  prog = "concatenate-and-print-files",
  description = "The cat utility reads files sequentially, writing them to the standard output."
)

parser.add_argument("path", help = "The file to read and print")

args = parser.parse_args()

print(args.path)