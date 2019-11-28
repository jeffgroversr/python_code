import json
import requests
import pandas as pd
import csv
import sys 

stdoutOrigin=sys.stdout 
sys.stdout = open("data/recrusion_ex2.csv", "w")

response = requests.get("https://api.usa.gov/crime/fbi/sapi/api/agencies?api_key=iiHnOKfno2Mgkt5AynpvPpUQTEyxE77jo1RU8PIv")
print(response.status_code)

response1 = response.json()
#print(response1)

#creates and saves the json file
with open('data/fbi_data.json', 'w') as f:
    json.dump(response1, f, indent = 4)
f.close()
#print(type(response1))	

f = open('data/fbi_data.json')
data = json.load(f)
f.close()

def myprint(data):
    for k, v in data.items():
        if isinstance(v, dict):
            myprint(v)
        else:
            print("{0}, {1}".format(k, v))
myprint(data)

sys.stdout.close()
sys.stdout=stdoutOrigin
