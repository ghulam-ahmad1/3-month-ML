import pandas as pd
import matplotlib.pyplot as plt
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
print(df.info())