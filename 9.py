# change the 'p' within spam to 'l'
# using only slicing and concantenation

S = 'spam'

pre_data = S[:1]
post_data = S[2:]

S = pre_data + 'l' + post_data
print S
