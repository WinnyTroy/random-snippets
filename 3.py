# -*- coding: utf-8 -*-

# get the frequency of each word in the string and make a list of dictionaries
# with the word being the key and it’s frequency as the value


# split the string into a list of words
# then create a dictionary where the keys=words : values=number_of_occurences
import string

line = "The quick brown fox jumps over the lazy dog"
data = string.split(line)
# wordfreq = str(data.count(data))
wordfreq = []

for word in data:
    wordfreq.append(data.count(word))
print dict(zip(data, wordfreq))
