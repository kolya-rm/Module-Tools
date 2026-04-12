content = "this is a list of words"
char = "i"

words = content.split(" ")

filtered_words = list(filter(lambda word: char in word, words))
print(filtered_words)