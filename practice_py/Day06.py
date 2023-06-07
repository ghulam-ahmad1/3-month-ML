print('Day 06 start Here !! \n')
print('Sets & Dictionaries \n' )

print('SETS\n')
s1={1,2,3,4,4,"Ahmad"} # As you can see Duplicat Element can't be in Set 
print(s1)

print('By For Loop ')
for x in s1 :
    print(x)
print('By While Loop ')

'''
i=0
while i<len(s1):
    print(i,';',s1[i])
    i+=1
'''
s1.add('Muneeb') # that is new 
print(s1)
s2={'Apple','mango'}
print('Ahmad' in  s1)
print(1 in s1)

# adding set into set :
s1.update(s2)
print(s1)

l1=[1,2,3,4,5,'Yohohooo']
t1=(9,7,9,57)
#s1.update(l1)
s1.update(t1)
s1.remove('Ahmad')
print(s1)
del l1
del t1
print(s1)
'''
y=input('Enter string')
if y in s1 :
    print('it is there !!')
  ''' 
print('\n Dictionaries \n')
mydict={"name":"supra" , "model":"1990",
        'list' : ["Ahmad", "rajab" ,'Brother']}
print(mydict)
print(mydict['name'])
# Duplicates are nmot allowed 
# you can acess the List Like this present in the dictionary : 
[print(mydict['list'][0]),print(mydict['list'][2])]

print('\nFetching by for loop :')
for a in mydict :
    print(a , ':' , mydict[a] , ':' , type(a))

print('\nLength : ')
print(len(mydict))

print('\nonly values of Dictionary')
for x in mydict.values():
    print(x,": Type is : " ,type(x))
print('\nonly keys of Dictionary')
for y  in mydict.keys():
    print(y)
print('\nonly Both Keys & values of Dictionary')
for x , y in mydict.items():
     print(x,'->',y)    
print('\nPrinting the Keys :: ')
k=mydict.keys()
print(k)
print(type(k))
print('\nprinting the Values :')
v=mydict.values()
print(v)
print(type(v))
mydict['name']="Supra MK4"
print(mydict)

# casting in Dictionaries  ::
print(type(int(mydict['model'])))
print(mydict)
