# -*- coding: utf-8 -*-
"""
Created on Wed May 31 09:01:29 2023
Day_04 | Ghulam Ahmad | 
"""
lst=list(("Ahmad","Rajab","Ghulam"))
print(type(lst))
print(lst[-2])
print(lst[0])
print(lst[0:2])
print(lst[0:-1])
print(lst[-1:0])
print(lst[0:-2])
print('\n Slicing Furthur : Repitition ')

ls=["Muneeb","Ahmad","Ghulam","rajab"]
ls[1:3]=["Ghulam Ahmad"]
#ls[1:2]=["Yoyo","Bruh"]
print(ls)
print(len(ls))
# Extending the list :
ls.extend(lst)
print(ls)
#Sorting of List
ls.sort()
print(ls)

ls3=ls
print(ls3)
ls3.remove("Ahmad")
print(ls3)
ls3.pop(0)
ls3.pop() # pop from last :
print(ls3)
del ls3[1]
print(ls3)
# Clearing all the lements of List  : 
lst.clear()
del lst # Deleted Totaly : 
ls.clear()
print(ls)
'''
# Small Program : 
ls1=["Ahmad","Ghulam","rajab","muneeb"]
print("This is the List : ")
print(ls1)
x=input("Enter the string : ")
if x in ls1:
    print('Executing Loop : ')
    for i in x:
        print(i)
else:
    print("Its not Present there !!!")
'''

# Trying New Things : 
print("\n")
print('Using For loop :')
list1=["X-man" , "Mutant" , "Spacex"]
for i in range(len(list1)):
    print(i," : ",list1[i])

print('Using while Loop :')
x=0
while  x < len(list1) :
     print(x,':',list1[x])
     x+=1
     
# List Comprehensions 
print('List Comprehensions way :')
[print(x) for x in list1]
list2=[5,3,6,33,7,4,78,3,7,4,7]
list2.sort(reverse=True)
print(list2)

# List Copied ;
l2=list2.copy()
print(l2)

# its append values at start :
L1=[1,2,3]
l2=[4,5,6]
for x in L1:
    l2.append(x)
print(l2)
