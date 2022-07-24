
# If-else statments

wheel = 15
track = 3

if wheel > track
    print(wheel)

# another example
level = 120
myExperience = 130

if myExperience > level:
    print("You have gained a level.")
elif level == myExperience
    print("You are still at your current level.")
else:
    print("No changes have been made to your level.")

# Are you old enough?
a = 18
b = 22
if a > 17 print("You can get a driver's license.") if b > 21 print("You can purchase alcohol")

# And, Or Operators
a = 18
b = 22
c = 10
if b > a and c < a:
    print("You can get a driver's license and have the right to buy alcohol.")
# using or
a = 18
b = 22
c = 10
if b > a or c < a:
    print("You may be eligible to drive or get alcohol.")

x = 90,000

if x > 30,000:
    print("You are eligible to buy a sedan or compact car.")
if x > 50,000:
    print("You can buy a mid-end car.")
if x > 100,000:
    print("You can buy a luxury car.")
else:
    print("Can you tell me how much money you have first?")

# while and for loops
i = 10
while i < 15:
    print(i)
    i += 1
# for loop
i = 4
for (i = 0; i < 6; i++){
    print(i)
}

# range function --> use this to loop your code for a given period
for y in range(9):
    print(y)

# range function with more than one parameter
for y in range(9,12):
    print(y)

# nested loops
gameConsole = ["slim look","black","dvd drive"]
bookReader = ["very small","portable","long battery life"]

for x in gameConsole:
    for y in bookReader:
    print (x,y)

# Functions

def myFunction(brand,tablet,definition):
    print("My device is from" + brand + "It is a small:" + tablet + "The graphic quality is" + definition)

myFunction("Susd","efe","High definition")
myFunction("Duda","gen 2", "Standard definition")

# passing a list as an argument
def your_Function(diet):
    for diet in yourFunction:
        print(diet)
    diet = ["vegetarian","keto","fasting"]
yourFunction(diet)

# Python lambda function takes any number of arguments
# lambda arguments : expression

# arrays
myTrucks = ["Charlie", "Lucky","Goldy"]
# assign
z = myTrucks[1]
# reassignment
myTrucks[0] = "Charles"

#find length
print(len(myTrucks))

# adding array element
myTrucks.append("Roxane")

# Python Classes
class MyRecipe:
    tablespoons = 10
# create object
    r1 = myRecipe()
    print(r1)

class Gamer:
    def _init__(self,hairstyle,age):
        self.hairstyle = hairstyle
        self.age = age
    g = Gamer("messy","sixteen")

    print(g.hairstyle)
    print(g.age)

# Object methods