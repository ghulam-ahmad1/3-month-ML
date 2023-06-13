import numpy as np
print('Day 02 of Practicing Numpy  : ')
# Numpy Indexing  :
arr=np.array([1,2,3,4,5,6])
print(arr)
print(arr[0])
print(arr[1])

# Can Also add Elements Like this : 
print(arr[1]+arr[2])

# Accessing 2-D array :
arr1=np.array([[1,1,1,1,1],[2,3,4,5,6]])
print('Dimensions in arr1 are : ',arr1.ndim)
print(arr1[0][1])
print('Negative Indexing  ; ',arr1[0,-1])

# Accessing 2-D Arrays:
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr2[0,1,2])
print(arr2[0,0,0])

# Slicing of the Arrays  : 
print(arr[-3:-1]) # Including the Indexes !

print(arr1[1,1:2])
print(arr1[0:2,2])