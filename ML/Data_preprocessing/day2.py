import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import seaborn as sb
# Now Lets start Preprocessing  :

X=pd.read_csv("iris.csv")
# print(X.info())
# print(X.describe())
# print(X.isnull().sum())
df=pd.DataFrame(X)
# print(df.corr())
# selecting the Dependent and indepent values :
A=df.iloc[:,0:4].values
B=df.iloc[:,-1].values
# A=pd.get_dummies(A, dummy_na=True)
# print(A)
# le=LabelEncoder()
df.plot()
df.hist()
plt.show()
