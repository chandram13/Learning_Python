
# Python File Handling

# open() function to work with files
# takes paramaters: filname, mode

x = open(filename,mode)

# four methods for opening a file
# "r" Read, "a"-append, "w"-write,"x"-create

e = open("firstFile.txt","rt") # read text "firstFile.txt"

# reading files

r = open("firstFile.txt")
print(r.read())

# then close the file
r.close()

# File writing, write to an existing file
f = open("firstFile.txt","a")
f.write("Now this file has more text")
f.close()

# open and read the file
f = open("firstFile.txt","r")
print(f.read())

# overwriting the content
f = open("firstFile.txt, "w")
f.write("The file contains this string now.")

# open and read the content
f = open("firstFile.txt","r")
print(f.read())

f = open("secondfile.txt","x")
# now secondfile exists

# Deleting a file
import os
os.remove("firstfile.txt")
os.remove("secondfile.txt")



