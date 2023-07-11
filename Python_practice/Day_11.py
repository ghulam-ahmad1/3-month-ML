print('Day 11 Starts Here !!!')
# built in functions in python  used in classes
# Today we studeid about the CNN's Some methods Like :
# -> padding & -> stride  Availaible in book . chap #07
# also I Learn about the classes  :
'''class myclass :
    def __init__(self,name,age):
        self.name=name
        self.age=age
x=input('Enter your name  : ')
y=int(input('Enter your name  : '))
cls=myclass(x,y)
print(cls.age)
print(cls.name)'''
# There is also str() built-in function in python , Returned in string :
'''class prac_1:
    def __init__(self,cls,rollno):
        self.cls=cls
        self.rollno=rollno
    def __str__(self):
        return f'My class is  : {self.cls} & roll Number is  : {self.rollno} ,Thanks ! '
t=input('Enter class  : ')
q=input('Enter Roll Number : ')
cls1=prac_1(t,q)
print(cls1)
del cls1'''
# Objects can also contain methods. Methods in objects are functions that belong to the object.
'''class prac_2 :
    def __init__(self,y,o ):
        self.y=y
        self.o=o
    def myfunc(self):
        print("My name is  : " + self.y)
c=prac_2(' Ghulam Ahmad  ' ,100)
c.myfunc()'''

# self is not fixed you can call it anything :
class myclass :
    def __init__(obj,cls,h):
        obj.cls=cls
        obj.h=h
    def func(obj):
        print('my name is  : ' + obj.cls)
p=myclass('Ahmad' , 20)
# we can modofy the Object  properties :
p.cls='Ghulam Ahmad'
p.func()
# deleting the Object properties  :
del p.h


