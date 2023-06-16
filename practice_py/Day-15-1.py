def myfun(x):
    print("My name is  : " + x)
# for images date and time  :  
import datetime

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
print(x)
  
# Some built-in math Functions : 
import math as mt
a = min(1,2,3,4,5)
b = max(1,2,3,4,5)
print(b)
print(a)
y=mt.pi
print(y)
u=int(mt.sqrt(16))
print(u)

'''JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation'''

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])
print(type(y))

# WE can Convert into JSON
#  like this   : 
mydict={"name":"Ghulam Ahmad", "class":"BSEE" ,"age":20}

# conerting into the Json : 
j=json.dumps(mydict)
# The Results will be a Json String  : 
print(j)
print(type(j))

# We can Convert many Datatypes into the Json's String .
# Aslo JSON mostly used in Machine Learning  :  

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))
