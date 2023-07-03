import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

X=pd.read_csv('abc.csv')

plt.scatter(X['distance'], X['price'] )
x = X['distance'].values[:, np.newaxis]
y=X['price']
lr=LinearRegression()
lr.fit(x, y)

print(lr.predict([[25]]))

print(lr.coef_)

print(lr.intercept_)

t=lr.coef_*25+lr.intercept_  # this lines tell us about that what regression coeficient and intwercept is ? 


''' Multiple Linear Regression '''


data = pd.read_csv('abcde.csv')

X=data[['distance','years']]
y=data['price']

from sklearn.model_selection import train_test_split

X_train , X_test , Y_train , Y_test = train_test_split(X,y,test_size=0.2 ,random_state=10)

cl=LinearRegression()
cl.fit(X_train, Y_train)
print('Predicted Values of  Test data ',cl.predict(X_test))
print(cl.score(X_test, Y_test)) # Accuracy of Model  on test data

