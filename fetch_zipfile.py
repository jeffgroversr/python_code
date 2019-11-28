#https://stackoverflow.com/questions/37604589/how-can-i-download-a-zipped-file-from-the-internet-using-pandas-0-17-1-and-pytho?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

from zipfile import ZipFile
from urllib.request import urlopen   
import pandas as pd
import os

URL = \
    'https://aqs.epa.gov/aqsweb/airdata/daily_44201_2018.zip'

# open and save the zip file onto computer
url = urlopen(URL)
output = open('daily_44201_2018.zip', 'wb')    # note the flag:  "wb"        
output.write(url.read())
output.close()
    
df = pd.read_csv('daily_44201_2018.zip')   # pandas version 0.18.1 takes zip files  
