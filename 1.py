integers = []

for x in range(0, 1000):
    if (x % 3 == 0 or x % 5 == 0):
        integers.append(x)
print(integers)


our_list = [x for x in range(1000) if x % 3 == 0 or x % 5 == 0]
print(our_list)
