import pandas as pd
df = pd.read_csv("convertcsv.csv")
#total = df.isnull().sum()
drop = df.dropna(axis=1 , thresh = 2)
print (drop) 