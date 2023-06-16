# Polymorphism is used when we have the multiple classes with same methods :
# Like in the Example Given Below  :

# Also We Use inheritance in Polymorphism  : Like This  :
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("move")


class Car(Vehicle):
    pass
#   def move(self):
#     print("Drive!")


class Boat(Vehicle):
    #   def __init__(self, brand, model):
    #     self.brand = brand
    #     self.model = model
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    #   def __init__(self, brand, model):
    #     self.brand = brand
    #     self.model = model
    def move(self):
        print("Fly!!")


car1 = Car("Supra", "MK4")  # Create a Car class
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat class
plane1 = Plane("Boeing", "747")  # Create a Plane class

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()

''' | python Scope | '''
# A variable is only available from inside the region it is created. This is called scope.

print("\nScope in python : \n")


def myfun():
    x = 100

    def myinnerfun():
        print(x)
    myinnerfun()


myfun()

# Global Scope  :
y = "Ghulam Ahmad"


def myfun1():
    print(y)


myfun1()

'''If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):'''
def myfun2():
    x=200
    print(x)
myfun2()
print(y)

# Using 'global' Keyword : 
t=1000
def func() :
    global t
    t= 100
func()
print(t)

# import   as my
# my.myfun('Ghulam Ahmad')
