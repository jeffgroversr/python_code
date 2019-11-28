#https://stackoverflow.com/questions/46098931/pandas-calculate-change-across-rolling-timeframe

import pandas as pd
import csv
############################### % Rolling Averages##########################

from myfunctions import newid, newid1, idchange
df = pd.read_csv(newid)
print(df.head())

df['change'] = df[idchange].pct_change(periods=12)

print(df)
df1 = df.dropna()
df2 = df1.tail(300)

df2.to_csv(newid1, index=False)
df3 = pd.read_csv(newid1, squeeze=True, index_col=None)
df4 = df3[["DATE","change"]]
#print(df4)


from myfunctions import newid2
df4.to_csv(newid2, index=False)
df4.to_excel(data/AAAFF.xlsx)
print(df4.head(20))

############################
