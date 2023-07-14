import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

# Reading the csv file  : 
ds = pd.read_csv("50_Startups.csv")
 
# Separating  the dependent and independent variables
X=ds.iloc[:,:4].values
y=ds.iloc[:,-1].values

# we have catagorical variables we have to encode them 
from sklearn.preprocessing import LabelEncoder , OneHotEncoder
lablencoder_X=LabelEncoder()
X[:,3] = lablencoder_X.fit_transform(X[:,3])
'''In New Release'''
# onehotencoder=OneHotEncoder(categorical_features=[3])
# onehotencoder = OneHotEncoder(categorical_features=[3])
from sklearn.compose import ColumnTransformer
# Country column
ct = ColumnTransformer([("State", OneHotEncoder(),[ 3])], remainder = 'passthrough')
X = ct.fit_transform(X)

# Avoiding the Dumy  Variable Trap :
X=X[:,1:]

#Splitting the Dataset into the training and testing Data  ; 
from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test  = train_test_split(X,y,test_size=0.2,random_state=0)

# Fitting the Multiple Linear Regression to Training set 
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)
#Predicting the Test data :
y_pred = regressor.predict(X_test)

#Accuracy of Model
score=regressor.score(X_test, y_test)

