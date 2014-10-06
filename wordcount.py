from sys import argv
import string

word_counts = {}

script, filename = argv

with open(filename) as f:
    for line in f:
        words_in_line = line.strip().split()
        for word in words_in_line:
            word = word.strip(string.punctuation).lower()
            word_counts[word] = word_counts.get(word, 0) + 1


for word in sorted(sorted(word_counts), key=word_counts.get, reverse=True):
    print word, word_counts[word]

#for word in sorted(word_counts, cmp=lambda x,y: cmp(word_counts[x], word_counts[y]), reverse=True):
#    print word, word_counts[word]

# frequency_dict = {}
# for word in word_counts:
#     frequency = word_counts.get(word)
#     frequency_dict[frequency] = frequency_dict.get(frequency, []) + [word]

# for frequency in sorted(frequency_dict, reverse=True):
#     print_list = frequency_dict.get(frequency)
#     for word in sorted(print_list):
#        print word, frequency