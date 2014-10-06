from sys import argv
import string

word_counts = {}

script, filename = argv

with open(filename) as f:
    for line in f:
        words_in_line = line.strip().split()
        for word in words_in_line:
            word = word.strip(string.punctuation)
            word_counts[word] = word_counts.get(word, 0) + 1
for word, count in word_counts.items():
    print word, count