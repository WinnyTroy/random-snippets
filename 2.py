# # a.) list of squares of values that are integers only from the list above

second = [1, 4, 8, 20, 33, 20, 23, {3: 33}, {4: 44}, "mango", "coconut"]

dup = second[:7]

for x in dup:
    x *= 2
    print(x)


# b.) list of dictionaries for values that are dictionaries with the key cubed and the value raised to power 5

for x in second[7:9]:
    for v in x.values():
        final = v ** 5
    print final



# c.) Extract a list of fruits from the list above

for x in second:
    if type(x) == str:
        print(x)
