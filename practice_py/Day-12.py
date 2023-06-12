# print('Day #12 Starts here !!')
# print('''Inheritance allows us to define a class that inherits all the methods and properties from another class.
#
# Parent class is the class being inherited from, also called base class.
#
# Child class is the class that inherits from another class, also called derived class.''')
#

print('Creating a Parent Class  : ')
class person :
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def my_func(self):
        print('My first name is  : ',self.fname ,'& Last name is : ',self.lname)
x=person('Ghulam','Ahmad')
x.my_func()
print('Creating teh childe Class  : ')
# class student(person):
#     pass
# x=student('Rajab','Mustafa')
# x.my_func()
class student (person):
    def __init__(self,fname,lname):
        # person.__init__(self,fname,lname) # for inheriting the peroperties of parent class
        super().__init__(fname,lname) # inherit all the properties :
        self.graduate=2025
    def func_1(self): # Adding the Methods in the child class :
            print('I am an:',self.fname+self.lname,' Engineer and my year of graduation is  : ',self.graduate )
y=student('M','L')
# y.my_func()
# print('My graduation year is : ',y.graduate)
y.func_1()
