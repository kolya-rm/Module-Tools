import argparse

parser = argparse.ArgumentParser(
  prog = "count-containing-words",
  description = "Counts words in a file that contain a particular character",
)

parser.add_argument("-c", "--char", help = "The character to search for", default = "e")
parser.add_argument("path", help = "The file to search")

args = parser.parse_args()

with open(args.path, "r") as f:
  content = f.read()

words = content.split(" ")
filtered_words = list(filter(lambda word: args.char in word, words))
filtered_words_count = len(filtered_words)

print(filtered_words_count)