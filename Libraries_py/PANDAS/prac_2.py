import pandas as pd
df  = pd.read_csv("sample.csv")
print(df)
print('\n')
# finding the Correlation Between the columns  :
print(df.corr())