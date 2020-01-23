#https://stackoverflow.com/questions/52085191/modulenotfounderror-no-module-named-pyodbc-when-importing-pyodbc-into-py-scri
#https://datatofish.com/how-to-connect-python-to-sql-server-using-pyodbc/
#https://www.microsoft.com/en-us/download/details.aspx?id=56567


import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DATABASESERVER,1433;'
                      'Database=Medicare;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM Medicare.dbo.newdata')

for row in cursor:
    print(row)