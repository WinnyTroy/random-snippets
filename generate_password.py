import random

alphabet = 'abcdefghijklmnopqrstuvwxyzAEIOU'
my_pw = ''
pw_length = input('How many digits would you require for your password: ')

for num in range(pw_length):
    x = random.randrange(len(alphabet))
    y = random.randint(0, 10)
    my_pw = my_pw + alphabet[x] + str(y)

print my_pw
