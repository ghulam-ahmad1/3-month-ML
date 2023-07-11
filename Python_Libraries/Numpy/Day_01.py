
import numpy as np
print('starting the Numpy : ')
arr=np.array([1,2,3,4,5,67])
print(arr)

# Numpy Creating Arrays : 
# Its a Numpy ndarray ; 
print(type(arr))

arr1=np.array((1,2,3,4,5))
print(type(arr1), 'We Converted the Tuple into the  ndarray !')

# 0D Array : 
arr2=np.array(100)
print("0D_Array :  ",arr2)

# 2-D Arrays :  Also  matrix : 
arr3=np.array([[1,2,3],[4,5,6]])
print(arr3)

# 3-D Arrays [often use to represent Tensor : ]
arr4=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr4)

# you can also check the Number of Dimensions :  by using  :  'ndim'
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)

# you can define any Array can have any Number of Dimensions  :  Like Given below  :
arr5=np.array([1,2,3,4,5],ndmin=5)
print(arr5)
print('dimesions of the arr5 is  : ',arr5.ndim)
