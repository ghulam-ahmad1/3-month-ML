print("Day-07 start Here !!\n")
print("We did intro to Machine Learning that day, we Learn about the Work of Machine Learning !!")
print("Day #08 starts | 6th June 2023 | Ghulam Ahmad \n")

# Nested Dictionaries "
print('Nested Dictionaries : ')
dict1={'info ':{'name':'ahmad', 'age': 20} ,
        'info1' : {'name' : 'Rajab', 'age':18 }
        }
print(dict1)
# Accessing the Elements of the Dict..
print(dict1['info ']['name'])

print('\nUsing the For loop  : ')
for x , y in dict1.items() :
    print('[key :',x,']:','[Vaule :',y,']')

info0={'name': 'Muneeb' , 'age':20}
info2={'name':'waleed' , 'age':19 }
allinone={
    'info0':info0,
    'info2':info2
}
# Acessing:
print('\n'+allinone['info0']['name'])
'''
a=int(input("Enter number a :"))
b=int(input("Enter number b :"))
c=int(input("Enter number c :"))
if a<b:
    print(f'{a} is small')
elif a==b==c:
    print('All are equal .')
elif a == b:
    print(f'{a} is equal to {b}')
else:
    print(f'{b} is smaller than: 'f'{a}')
'''
# While loop  :
i=1
while i < 11:
    print(i)
    i+=1
else:
    print(f'Now i : [{i}] is no longer Less than 11 ')

