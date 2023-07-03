# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 10:01:26 2023

@author: Dell
"""

import pandas as pd
from numpy import set_printoptions
from sklearn import preprocessing
#reading the  file 
x=pd.read_csv('purchase.csv')

# taking info 

#print(x.info())

# describe Data 

#print(x.describe())

x['Ball'] = x['Ball'].fillna(x['Ball'].mean())

x['Bat'] = x['Bat'].fillna(x['Bat'].mean())

x['apple'] = x['apple'].fillna(x['apple'].std())

x['Orange'] = x['Orange'].fillna(x['Orange'].min())

x['Price'] = x['Price'].fillna(x['Price'].max())

# Now using the other Libraries 
# Lets see !!

Data = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv'
name = ["Romaan","kamran","asad","Dawood","Emad","Faizan","Gohar","Habib","Irfan"]
data = pd.read_csv(Data , names=name)

scaler = preprocessing.MinMaxScaler(feature_range=(0,2))
rescaled = scaler.fit_transform(data)
set_printoptions(precision=5)

from sklearn.preprocessing import StandardScaler
data_scaler = StandardScaler().fit(data)
data_rescaled = data_scaler.transform(data)
data_rescaled

from sklearn.preprocessing import StandardScaler
data_scaler = StandardScaler().fit(data)
data_rescaled = data_scaler.transform(data)
data_rescaled