# # Order the list

values = [1, 3, -20, -100, 200, 30, 201, -200, 9, 3, 4, 2, -9, 92, 99, -10]

# # a.) In ascending Order

values.sort()
print values


# # b.) In descending Order

values.reverse()
print(values)


# # c.) Get the maximum number in the list

print max(values)

# # d.) Get the minimum number in the list

print min(values)


# # e.) Get the average of the list

average = sum(values)/len(values)
print average

# f.) list of dictionaries from the list with the key being the absolute value of an element and the value being the cube of that element

final = []


for x in values:
    ans = zip(str(abs(x)), str(x**3))
    final.append(ans)
print final
