# Applying the Simple Linear Regression on Data set :
import  pandas as pd
import  numpy as np
import  matplotlib.pyplot as plt

ds = pd.read_csv("Salary_Data.csv")
X=ds.iloc[:,:-1].values # independent Vaiable
y=ds.iloc[:,-1].values # Depebdent Variable

# Splitting the Data set  ;
from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test  = train_test_split(X,y,test_size=0.2,random_state=0)

# fitting the simple Linear Regression to the Trainig set
from sklearn.linear_model import  LinearRegression
reg= LinearRegression()
# fit method :
reg.fit(X_train,y_train)

# predicting test set Results :
y_pred = reg.predict(X_test)
score = reg.score(X_test,y_test)

#Visualizin the Trainig set results :
plt.scatter(X_train, y_train, color="red")
plt.plot(X_train,reg.predict(X_train),color="blue")
plt.title("Salary vs Experience [Traing set]")
plt.xlabel("Experience")
plt.ylabel("Salaries")
plt.show()

#Visualizin the Test set results :
plt.scatter(X_test, y_test, color="red")
plt.plot(X_train,reg.predict(X_train),color="blue")
plt.title("Salary vs Experience [Test set]")
plt.xlabel("Experience")
plt.ylabel("Salaries")
plt.show()

