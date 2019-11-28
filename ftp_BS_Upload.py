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