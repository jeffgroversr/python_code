#https://pythonprogramming.net/ftp-transfers-python-ftplib/
#https://stackoverflow.com/questions/11768214/python-download-a-file-over-an-ftp-server/12424311
#Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32

from ftplib import FTP

import shutil
import urllib.request as request
from contextlib import closing

with closing(request.urlopen('ftp://ftp.ngdc.noaa.gov/Solid_Earth/cdroms/TerrainBase_94/document/america.txt')) as r:
    with open('america.txt', 'wb') as f:
        shutil.copyfileobj(r, f)
		