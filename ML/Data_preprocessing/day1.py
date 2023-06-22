import pandas as pd
import matplotlib.pyplot as plt
'''Working on iris Data set  |  Data Set From Kaggel '''
df = pd.read_csv("iris.csv")
# print(df)
# print(df.info())
'''newdf=df.dropna() # it will ignore the NULL values or ROws  will be removed .
# print(newdf)
print((newdf.info()))'''
# we can also replace the empty places with some value
# WE can Also Replace the NAn values with the Mean
# X=df['Calories'].mean()
# df["Calories"].fillna(X,inplace=True)
# df['Date']=pd.to_datetime(df['Date'])
# df['Date'] = pd.to_datetime(df['Date'])
# df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
# print(df.isnull().sum())
# print(df.info())
# df["sepal_length"].hist()

# --------- #
# To Display Stats About the Data  .
print(df.describe())

# Now I wanted to Display the Samples of Each Class  :
print(df["species"].value_counts())
# species = ['Iris-setosa','Iris-versicolor','Iris-virginica']
# Now checking the Null value if there are any in Data set  :
df["species"].hist()
plt.show()