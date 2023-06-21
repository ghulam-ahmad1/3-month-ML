import matplotlib as mt
import matplotlib.pyplot as plt
import numpy as np
# print("Version : ",mt.__version__)
#
# x=np.array([2,4,6,3,9])
# y=np.array([2,5,6,8,2])
# plt.subplot(1,2,1)
# plt.plot(x,y)
# # Labling the Axis  :
# plt.title("Practicing Plot")
# plt.xlabel("x-Axis")
# plt.ylabel("Y-Axis")
# plt.grid() # Adding Grid
# plt.show()
# '''
# # For multiple Points  :
# a=np.array([1,3,6,8])
# b=np.array([4,8,5,7])
#
# plt.plot(a,b)
# plt.show()
#
# # if we donot Speciy the X-axis Points it genreate automatically Like this :
# # Also Specifying the Markers  :
# # plt.plot(b , marker='o')
# # plt.plot(b,'o:r')
# # you can also Define the Maker Size  :  as  'ms'
# plt.plot(b,'o-',ms='8')
# plt.show()
#
# # you can Also perform any many function on markers . watch that on W3schools !!
#
# # Also we can define many Lines Like this  ;
# y1=np.array([3,5,4,7])
# y2=np.array([9,6,4,3])
# plt.plot(y1)
# plt.plot(y2)
# plt.show()
# '''
# # you can also draw multiplt plots in one Figure  :
#
# y1=np.array([3,5,4,7])
# y2=np.array([9,3,5,3,8])
# plt.subplot(1,2,2)
# plt.plot(y1,y2)
# plt.show()
#plot 1:
'''x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()
'''

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
plt.pie(y, labels = mylabels , shadow=True , explode=myexplode )
plt.legend(title="fruit name" , bbox_to_anchor=(0.95,1.025), loc="upper left")
plt.show()

