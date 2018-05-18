# -*- coding: utf-8 -*-

# get the frequency of each word in the string and make a list of dictionaries
# with the word being the key and it’s frequency as the value


# split the string into a list of words
# then create a dictionary where the keys=words : values=number_of_occurences


line = "The quick brown fox jumps over the lazy dog"
data = line.split(' ')
wordfreq = str(data.count(data))


for key in wordfreq:
    import pdb;
    pdb.set_trace()
    print key, data['key']
