print("Numpy Continued :  ")
import  numpy as np
x=np.array([[1,2,3,4],[5,6,7,8]])
print(x)
# Data types on Numpy  :
print(x.dtype)
f=np.array(x,dtype='S')
print(f.dtype)
print(f)

arr= np.array([1,2,3,4],dtype='i4')
print(arr.dtype)
print(arr)

newarr= arr.astype("S")
print(newarr.dtype)

arr1= newarr.astype(bool)
print(arr1.dtype)
print(arr1)

# Copy and View in Numpy  :
a=arr1.copy()
a[0]=False
print(a)
print(arr1)

b=arr1.view()
print(b)
print(arr1)

# Array's shape  :
print(x.shape)

p = np.array(x,ndmin=5)
print(p.ndim)
print(p.shape)


# REshaping of Array  :
a1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
ar=a1.reshape(4,3)
print(ar)

# flatening of he aray
print('Array of  5 Dimensions is Flattened ')
print(p.reshape(-1))
print("Using the For Loop : ")
for i in x  :
    print(i)
# NEsted Loop :
print('Using the nested loop  on 2-D array :: ')
for n in x :
    for y in n :
        print(y)
k = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print('using Nested Loop in 3-d array  : ')
for x in k :
    for i in x :
        for y in i :
            print(y)
print('Using the Simple ForLoop   : ' )
for x in k :
    print(x)
# Built in Function  'nditer' for teh iteration in array   :
print("Using 'nditer' function in arrays  : ")
for x in np.nditer(k) :
    print(x)

# you can Aslo Join  the  arrays Like this :
r=np.array([1,2,3,4,])
o = np.array([5,6,7,8])
arr2=np.concatenate((r,o))
print(arr2)

# In stack all arrays have the same shape  :
# this is the stacking ALong the Column  :
arr3=np.stack((r,o),axis=1)
print(arr3)

# Stacking Along the Rows:
arr4=np.hstack((o,r))
print(arr4)
print(arr4.ndim)

# Built in function
for idx , i in np.ndenumerate(k) :
    print(idx, i)
