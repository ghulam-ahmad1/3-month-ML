import pandas as pd  
from matplotlib import pyplot as plt


ds=pd.read_csv("class_test_data.csv")

# Dealing with the Empty cells  ;

#print(ds.info())
''''  Dealing with the Empty cells  '''
# Empty cells are in the calories section  :
# Dealing with the calories section 

ds['Calories']=ds['Calories'].fillna(ds["Calories"].mean())
#print(ds)
#print(ds.info()) 
# Now Not any Empty Cell Left  : 

    
'''Deealing with Wrong Data fromate '''

ds['Caloreis']=pd.to_numeric(ds['Calories'])


'''Dealing with the Duplicates in the data '''

ds.drop_duplicates(inplace = True)

"Dealing with the Wriong data "

dw=ds["Duration"].mean()
# print(dw)

for x in ds.index :
    if ds.loc[x,"Duration"] >120:
        ds.loc[x,"Duration"] = dw

ds.plot()
plt.show()
