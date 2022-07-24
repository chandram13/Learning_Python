
# Python Iterators

# Iterator vs Iterable

myVeggies = ("broccoli","carrots","kale","celery")
myit = iter(myVeggies)
# we run next four times since we have four values saved to our tuple myVeggies
print(next(myVeggies))
print(next(myVeggies))
print(next(myVeggies))
print(next(myVeggies))

# looping through an iterator
for v in myVeggies:
    print(v)

# create an iterator
class myVeggies
   def _init__(self):
    self.count = 1 # count stands for number of veggies I have
    return self
def __next__(self):
    x = self.count
    self.count += 1
    return x

myClass = myVeggies()
myiter = iter(myVeggies)

# I have a total of three veggies
print(next(myiter))
print(next(myiter))
print(next(myiter))

# Python Math Rules
d = min(3,9,12)
e = max(10,14,18)

print(d)
print(e)
# absolute value
x = abs(-400)
print(x)

# Doing Powers
z = pow(5,2)
print(z) # expected output 5 x 5 = 25

# Factorials in Python
import math
f = 10
fact = math.factorial(f)
print(fact)

# JSON package
import json
myDict = '{"school":"XYZ","age":"eighteen","class size":"twenty"}

# parse through myDict
parsedDict = json.loads(myDict)

# print result
print(parsedDict["class size"])

# Ask for user input

characterName = input("Enter the name of your character here.")
print("Your selected character name is:" + characterName)

