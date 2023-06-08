# print('Day 10 starts here !!')
#
# # lambda arguments : expression
# print('practcing Lambda Function : ')
# x= lambda  a : a+90
# print(x(5))
#
# y=int(input('Enter a Number  : '))
# h=lambda r : r**2
# print(h(y))
#
# # can be used as in Expressions  :
# u= lambda  o,p : o*p
# print(u(2,3))
#
# # you can use Lamda function inside another function  :
# # Here is how you can do it  :
# def func_1(n) :
#     return  lambda t :t*n
# my_func=func_1(100)
# my_func1=func_1(45)
# print(my_func(100))
# print(my_func1(100))

print("Classes starts here !! ")
class myclass() :
    x = 100
# Here we create the Object named p  :
p=myclass
print(p.x)
print(myclass)
# init function is important in classes :
