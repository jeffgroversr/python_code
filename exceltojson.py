#https://anthonydebarros.com/2013/02/05/get-json-from-excel-using-python-xlrd/
import pyexcel_xlsx
import time
import json
import xlrd

from collections import OrderedDict
import simplejson as json
# Open the workbook and select the first worksheet
wb = xlrd.open_workbook('D:/Users/drjef/OneDrive/AllData/OpenData/12-Health/12-1-41-1-HCAHPS.xlsx')
sh = wb.sheet_by_index(0)
# List to hold dictionaries
cars_list = []
# Iterate through each row in worksheet and fetch values into dict
for rownum in range(1, sh.nrows):
    cars = OrderedDict()
    row_values = sh.row_values(rownum)
    cars['Hospital_Name'] = row_values[0]
    cars['Star_1'] = row_values[1]
    cars['Star_2'] = row_values[2]
    cars['Star_3'] = row_values[3]
    cars['Star_4'] = row_values[4]
    cars['Star_5'] = row_values[5]
    cars['Star_All'] = row_values[6]
    cars_list.append(cars)
# Serialize the list of dicts to JSON
j = json.dumps(cars_list)
print(j)
# Write to file
with open('data/HCAHPS.json', 'w') as f:
    f.write(j)

import shutil

shutil1 = "data/HCAHPS.json"
shutil2 = "D:/Dropbox/ggi Dropbox/json/HCAHPS.json"
shutil3 = "HCAHPS.json"
shutil.copy(shutil1, shutil2)
shutil.copy(shutil1, shutil3)
#ftp://eyeman@192.185.11.29/httpdocs/json_to_web/json
#https://pythonprogramming.net/ftp-transfers-python-ftplib/

from ftplib import FTP
#domain name or server ip:
ftp = FTP('192.185.11.29')
ftp.login(user='eyeman', passwd = 'N^OalK6C7ZUhP')

ftp.cwd('/httpdocs/json_to_web/json')

def placeFile():

    filename = r'HCAHPS.json'
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()

placeFile()

#https://stackoverflow.com/questions/28016444/ftp-library-error-got-more-than-8192-bytes
'''
with open(str_param_filename, 'rb') as ftpup:
    ftp.storbinary('STOR ' + str_param_filename, ftpup)
    ftp.close()
'''