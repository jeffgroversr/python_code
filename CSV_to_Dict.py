#https://overlaid.net/2016/02/04/convert-a-csv-to-a-dictionary-in-python/

import csv
import sys
import pprint
 
import pandas as pd
df = pd.read_csv('SEDM.csv')
SEDM = df.to_dict('records')
print(SEDM)
print(SEDM[0])
print(SEDM[0].keys())
print(SEDM[0].values())
for k in SEDM:
     print(k)
pprint.pprint(SEDM)

print(SEDM[0]['Event_A'])

