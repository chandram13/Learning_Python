# Python Inheritance

class Animal:
    def _init__(self,spec,wei):
        self.spec = species
        self.wei = weight

    def printdata(self):
        print(self.spec,self.wei)

    # create an object, then utilize a method

    x = Animal("lion","fifty pounds")
    x.printdata() # assigned function then called it

# create child class
    x = Kind("Rabbit","eight pounds")
    x.printdata()
    # then use init method
    class Kind(Animal):
        def _init(self,spec,wei)

# then add a call, keep inheritance present
    class Kind(Animal):
        def _init(self,spec,wei):
            Animal.init__(self,spec,wei)

    # adding properties to a class
    class Kind(Animal):
        def _init__(self,spec,wei):
            super()._init__(spec,wei)
            self.grownyear = 5
    a = kind("monkey","seventy pounds",8) # 8 is from the added element grownyear

# add methods
class Kind(Animal):
    def _init(self,spec,wei):
        Animal.init__(self,spec,wei)
class Kind(Animal):
    def _init__(self,spec,wei):
        super().init__(spec,wei)
        self.grownyear = 5
    def OurZoo(self):
        print("Welcome to Aang's zoo this identifies as: ",self.spec,self.wei, "and is :",self.grownyear," years old")








