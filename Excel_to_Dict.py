#https://www.tutorialspoint.com/How-to-convert-a-spreadsheet-to-Python-dictionary
#https://learn.co/lessons/excel-to-python

import pandas as pd
df = pd.read_excel('SEDM.xlsx')
SEDM = df.to_dict('records')
print(SEDM)
print(SEDM[0])
print(SEDM[0].keys())
print(SEDM[0].values())
for k in SEDM:
     print(k)