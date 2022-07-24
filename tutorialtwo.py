# Looping through a string

for x in "loopthroughthis":
    print(x)

# string length
length = "strlen"
print(len(length))

# check string
message = "In this message you will find,"

if "you" in message:
    print("The word you is present here")

# check if word not in given string
newMessage = "You got new mail"
print("check" not in newMessage)

newMessage = "You got new mail"
if "check" not in newMessage:
    print("I'm sorry, it's not there.")

# slicing
c = "I gotta go"
print(c[3:5])

# slicing from start
d = "Time to start"
print(d[:6])

# slice to the end
e = "Welcome home"
print(e[6:]);

# neg indexing
some = "ufogofig"
print(some[-6:-3])

# modify strings upper and lower
goli = "Good job, it's a goal!"
print(goli.upper())
fakra = "Oh man, we missed!"
print(fakra.lower())
# remove whitespace
fake = "Did we make a goal?"
print(fake.strip)

# replace
new = "It has a new screen and everything!"
print(new.replace("Nevermind, it's just preowned"))

# split use case
old = "My screen is described by: cracking, broken, and coming off"
print(old.split(":"))

# concatenating
old = "Preowned"
new = "Just Bought"
differences = old + " " + new
print(differences)

# formatting strings
mascot = "Mars"
area = "Very safe"
students = 100
schoolInformation = "XYZ Elementary + { } + { } + { }"
print(schoolInformation.format(mascot,area,students))

# important string methods

central = "We have the best food"
print(central.index("the"))

east = "We are smart"
print(east.join("especially in NY"))

