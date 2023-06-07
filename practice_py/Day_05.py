# Day 05 Started Here !! 
'''Tuples '''

tup=(1,2,3,4,5)
print(type(tup))
print(tup)

# can Also Write Tupes like this : 
t1='Ahmad','Rajab','muneeb'
print(t1)
print(type(t1))
print(t1[0])

print('\nBy For Loop : ')
for x in range(len(t1)):
    print(x,':',t1[x])

print('\nBy While Loop :')
i=0
while i<len(t1):
    print(i,':',t1[i])
    i=i+1

print(f'\nLength of this Tuple : {t1}  is :' , len(t1))

# Also Creat one tuple Like this  : 
t2=('Ahmad',) # it will be a tuple :
t3=('Rajab')# it will be a string :
print(type(t2))
print(type(t3))
'''
# Acessing the values in tuple : 
x = input('Enter String : ')
if x in t1 :
    print('it is present in the tuple !! ')
else : 
    print('Its not there !!')
# Tuple Constructure : 
'''
print('\n')
t_1=tuple((1,2,3,4,6))
print(type(t_1))

print('\n changing values in tuples  : ' )
tuple1=('Ahmad' , 100 , 'Rajab' , 99.99 , True)
print(tuple1)
y=list(tuple1)
print(y)
y[1]="Muneeb"
tuple1=tuple(y)
print(tuple1)

# Joining the Tuples : 
t0=t_1 + t1
print(t0)
#Multplying the tuples 
t_2=t0*3
print(t_2)

# Unpacking of the tuples :     
x4=('Mutant','Spacex','Suparco')
(x1,x2,x3)=x4
print(x1)
print(x2)
print(x3)
print(tuple1)

# Using of Astrisk (*)Sign :
# x7 has been assigned all the values which are left as a List :
x5,x6,*x7=tuple1  # its like filtring is happning : 
[print(x5),print(x6),print(x7) ,print('Type of X7 is :',type(x7))]

'''
Unpacking of List : 
lst = ["rtr",'er']
ls,l = lst
print(ls)
'''
#del t1  { Deleting the tuple | }
#print(t1) {Gives an error}

