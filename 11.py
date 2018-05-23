# Write a script that creates a new output file called myfile.txt
 # and writes the string "Hello file world!" into it.

f = open("test.txt", "w", "r")
f.write("Hello World!")

# write another script that opens myfile.txt
# and reads and prints its contents

q = open("test.txt")
print q
f.close()
