print('Day 4 strats here  :  ')
print('Numpy Continued  : ')
import  numpy as np

''' SPLIT THE ARRAYS '''
arr = np.array([1,2,3,4,5,6])
print(arr)
print(np.array_split(arr,3)) # This will return the 3 Array's in a List :
print(np.array_split(arr,4))

newarr = np.array_split(arr,5)
print(newarr)
print(newarr[0])# We can Acess the array Like this  :
print(newarr[1])

# Spliting the 2-D Array  :
arr1= np.array([[1,2,3],[4,5,6],[6,7,8],[9,10,11]])
newar= np.array_split(arr1,3)
print(newar)

# You can also Specify that on which Axis you Wanted to split :
a=np.array_split(arr1 , 3 , axis=1)
print(a)

# we Also have a function which split the Array along the rows  :
b=np.hsplit(arr , 3) # it Requires the Array to be Equaly Distributed :
print(b)

''' SEARCHING IN THE ARRAY  '''
# you can search an array to a certain Value  :
c=np.array([1,2,3,4,5,5,6,5,5])
print(np.where(arr==4)) # Indexex will be return
print(np.where(c==5)) # All the indexex where it is present   :

# We can aslo find the indexex where indexex are Even Like this  ;
print(np.where(c%2==0))
# to find the Odd one's :
print(np.where(c%2==1))

# 'Searcsorted()' it used in  sorted arrays   :
v=np.array([1,2,3,4,5,6,7,8,9])
x=np.searchsorted(v,6)
print(x)
# We can Search From teh Right side  ;
print(np.searchsorted(v,5,side='right'))
#Multiple Values of Searching  :
print(np.searchsorted(v,[3,4,5])) # --> Return the idexex
''' SORTING OF ARRAY'S '''
e=np.array([3,45,6,2,4,9,5,0,34])
print('Usorted : ',e)
print('Sorted  : ',np.sort(e))

''' NUMPY ARRAY FILTER  '''

print('\n ')
t=np.array([54,23,12,78])
u=[True,False,True,False] # True Values will be Filtered  :
n=t[u]
print(n)

# Creating the Filter array  :
# creatt an Empty List
p=[]

#go through the each element in array  ;
for x in t :
    if x > 40  :
        p.append(True)
    else :
        p.append(False)
n_arr=t[p]
print(n_arr)
# We can also create the filter array to find the Even Number  :
# We can Also Create Direct Filter From the Array  like this  :
s=t>40
n_arr1=t[s]
print("\n")
print(n_arr1)

# Also Another way of Filtering the Even Numbers  :
h=t%2==0
n_arr2=t[h]
print('Even Numbers Filtered  : ',n_arr2)