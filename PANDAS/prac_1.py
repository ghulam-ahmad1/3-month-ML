import pandas as pds
import matplotlib.pyplot as plt
# dataset = {
#     'cars' : ['supra','supramk4','buggati'] ,
#      'passing' : [1,23,4]
# }
# # present all the thingss in a Frame
# var=pds.DataFrame(dataset)
# print(var)
#
# print('Version : ',pds.__version__)
#
# '''  PANDAS SERIES  '''
# a = [1,3,4,5,6,7]
# var1=pds.Series(a)
# print(var1)
# print(var1[0])
# # we can Also specify the Index   :
# df=pds.read_csv("sample.csv")
# print(df)
df = pds.read_csv("best-selling-books.csv")
print(df)
# you can also plot like this  : 
# df.plot()
#This is a type of graph scattered plot : 
df.plot(kind = "scatter" , x='First published' , y = 'Approximate sales in millions')
plt.show()
df.info()