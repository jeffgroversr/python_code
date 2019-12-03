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
'''
# Function to convert a csv file to a list of dictionaries.  Takes in one variable called &quot;variables_file&quot;
#def csv_dict_list(SEDM):
# Open variable-based csv, iterate over the rows and map values to a list of dictionaries containing key/value pairs
 
reader = csv.DictReader(open('SEDM.csv', 'rb')
dict_list = []
for line in reader:
    dict_list.append(line)

#return dict_list
#csv_dict_list 
# Calls the csv_dict_list function, passing the named csv
 
#device_values = csv_dict_list(sys.argv[1])
 
# Prints the results nice and pretty like
 
#pprint.pprint(csv_dict_list)
'''