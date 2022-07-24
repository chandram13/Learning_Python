
# Python Dictionaries

myDict = {
    "wheels": "Hankoo",
    "rims": "spinning",
    "metal": "steel"
}
print(myDict)

# Getting items from a dictionary
print(myDict["wheels"])

# length
print(len(myDict))

# Accessing Dictionary Items
myBook = {
    "characters": "fictional"
    "plot": "three parts"
    "environment": "urban"
}
e = myBook["environment"]
f = myBook.get("environment") # to get the value of environment

g = myBook.keys()
print(g)

h = myBook.values()
myBook["plot"] = "two parts"

print(h)

# get all the values in the dictionary
i = myBook.items()
print(i)

# check if key exists
if "plot" in myBook:
    print("This story does have some story.")
else:
    print("This is garbage, turn it off.")

# Change dict items

racingGame = {"car": "zoom zoom", "course": "circuit", "time": "ten minutes"}
racingGame["racing course"] = "relay"

# update dictionary
racingGame.update({"racing course" : "dirt location"})

# adding items
racingGame = {"car":"zoom zoom","course":"circuit,"time":"eight minutes"}
racingGame["players"] = "eight"
print(racingGame)

# removing items
racingGame = {"car":"zoom zoom","course":"circuit","time":"fifteen minutes"}
racingGame.pop("car")

# removing the last inserted item
racingGame = {"car":"zoom zoom", "course":"circuit","time":"fifteen minutes"}
racingGame.popitem()
print(racingGame)

# deleting an item
racingGame = {"car":"zoom zoom", "course": "circuit","time":"fifteen minutes"}
del racingGame["course"] #-deleting the specific key-value pair
print(racingGame)

racingGame.clear() # clearing our dictionary racingGame
print(racingGame)

# Loop Dictionaries
cardGame = "number": "fifteen", "types": "six", "name": "fish"}
for c in cardGame:
    print(c)

# returning keys in dictionary cardGame
cardGame = "number": "fifteen","types":"six","name":"fish"
for c in cardGame.keys()
    print(c)

# looping through keys and values
for c,d in cardGame.items()
    print(c,d)

cardGame = cardGame.copy()
print(cardGame)

# Nested Dictionaries

myBrand = {
    "sedan" = {
        "name": "Charlie",
        "fit size": "four seats",
    }
    "truck" = {
        "name": "Coolah",
        "fit size": "two seats",
    "limo"= {
        "name": "Ghos",
        "fit size": "six seats"
    }
carCompany = {
    "sedan" : sedan,
    "truck": truck,
    "limo" : limo
}
print(carCompany)
    }
}


