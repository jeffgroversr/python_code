#https://www.youtube.com/watch?v=oQfNYqz8pLs&t=61s
import json
import requests
import pandas as pd
import csv
import sys 
import json
import shutil

with open('data/ftc_data.json') as f:       #{"data": [{"type":
    mydata = json.load(f)

question_access = mydata['data']
print(question_access)                     #[{'type': #Prints all types
print(type(question_access))   #<class list>

save_types = []
def get_all_types():
	for all_types in question_access: #This is a list
		user_types = all_types['attributes'] #This is a dictionary
		save_types.append(user_types)	#This puts all dictionary items in the file
get_all_types()

with open('data/all_type.json', 'w') as f:
	json.dump(save_types,f)

with open('data/all_type.json') as f:      
    mydata = json.load(f)
print(mydata)

type_data = pd.DataFrame(mydata) 
type_data.to_csv("data/all_types.csv")

############################################################
shutil1 = "data/all_type.json"
shutil2 = "D:/Users/drjef/OneDrive/AllData/OpenData/6-Consumer/6-1-20-6-1-all_type.json"
shutil3 = "data/dict_types.csv"
shutil4 = "D:/Users/drjef/OneDrive/AllData/OpenData/6-Consumer/6-1-20-6-1-dict_types.csv"
############################################################
shutil.copy(shutil1, shutil2)
shutil.copy(shutil3, shutil4)