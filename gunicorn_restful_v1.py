#Steps
#1. Add Link with correct ???_all
#2, Copy def and add ???all
#3. Add database name in def
#4. Change name in route

#def configure_app(app):
#    Configure Compressing
#        Compress(app)

#import flask_cache
#from flask_cache import Cache
#cache = Cache()
#https://stackoverflow.com/questions/43263356/prevent-flask-jsonify-from-sorting-the-data/43263483#43263483 
#https://docs.python.org/2/library/sqlite3.html
#Ref 1: https://stackoverflow.com/questions/3783238/python-database-connection-close

COMPRESS_MIMETYPES = ['text/html', 'text/css', 'text/xml', 'application/json', 'application/javascript']
COMPRESS_LEVEL = 6
COMPRESS_MIN_SIZE = 500

import itertools
import pyodbc 
import flask
from flask import request, jsonify
from flask_restful import Resource, Api, request
from flask import Flask
	
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False   #New line from Stackoverflow.com - See above
app.config["DEBUG"] = True
api = Api(app)

#conn = pyodbc.connect('Driver={SQL Server};'
#            		  'Server=DATABASESERVER,1433;'
#					  'Database=API_BayeSniffer;'
#					  'Trusted_Connection=yes;')
#cursor = conn.cursor()	
@app.route('/', methods=['GET'])
def home():
    return '''
<h1>Welcome to the BayeSniffer!</h1>
<p>Enjoy selecting posterior Probability of "Health" Things!</p>
<p><h3><a href="http://50.197.246.137:5000/bayesniffer_api/v1/resources/HAII/all" target="_new" title="Healthcare Associated Infections">Healthcare Associated Infections</a></h3></p>
<p><h3><a href="http://50.197.246.137:5000/bayesniffer_api/v1/resources/HAII?State=NC" target="_new" title="Healthcare Associated Infections-State=NC">Healthcare Associated Infections = NC</a></h3></p>
<p><h3><a href="http://50.197.246.137:5000/bayesniffer_api/v1/resources/HAII?State=NC&Provider=340053" target="_new" title="Healthcare Associated Infections-State=NC & Provider = 340053">Healthcare Associated Infections: State=NC & Provider = 340053</a></h3></p>
'''

@app.route('/bayesniffer_api/v1/resources/HAII/all', methods=['GET'])
def api_HAI_all():

	conn = pyodbc.connect('Driver={SQL Server};'
						  'Server=DATABASESERVER,1433;'
						  'Database=API_BayeSniffer;'
						  'Trusted_Connection=yes;')
	with conn:
	    cursor = conn.cursor()	

#	cursor.execute('SELECT * FROM API_BayeSniffer.dbo.HAI_Master;')
	cursor.execute('SELECT Hospital, Provider,Address,City,State,ZIP_Code,\
	    Start_Date,End_Date,HAI,Better,Worse,Same,Score,Rank\
	    FROM API_BayeSniffer.dbo.HAI_Master \
		ORDER BY HAI_Master.[Hospital];')

	desc = cursor.description
	column_names = [col[0] for col in desc]                      #This puts SQL date into json
	data = [dict(zip(column_names, row))  
			for row in cursor.fetchall()]
#	print(data)

	return jsonify(data)

@app.route('/bayesniffer_api/v1/resources/HAII', methods=['GET'])
def api_filter():

    conn = pyodbc.connect('Driver={SQL Server};'                    # Connection object #
                 		  'Server=DATABASESERVER,1433;'
		    			  'Database=API_BayeSniffer;'
			    		  'Trusted_Connection=yes;')
    with conn:
        cur = conn.cursor()	 #Once you have a Connection, you can create a Cursor object and call its execute() method to perform SQL commands. 
		                     #See ref 1,

    query_parameters = request.args	        #This is a Flask request object that stores all the parameter values
    Provider = query_parameters.get('Provider')
    Hospital = query_parameters.get('Hospital')
    State = query_parameters.get('State')
		
#    query = "SELECT * FROM API_BayeSniffer.dbo.HAI_Master WHERE"
    query = ('SELECT Hospital, Provider,Address,City,State,ZIP_Code,\
					Start_Date,End_Date,HAI,Better,Same,Worse,Score,Rank\
					FROM API_BayeSniffer.dbo.HAI_Master WHERE')
		
    to_filter = []                      #Initializing a dictionary of empty lists
    if Provider:
        query += ' Provider=? AND'
        to_filter.append(Provider)                   #SQL append clause
    if Hospital:
        query += ' Hospital=? AND'
        to_filter.append(Hospital)
    if State:
        query += ' State=? AND'
        to_filter.append(State)
    if not (State):
        return page_not_found(404)

    query = query[:-4] + ';'
	
    results = cur.execute(query, to_filter).fetchall()	

    desc = cur.description
    column_names = [col[0] for col in desc]                      #This puts SQL date into json
    data = [dict(zip(column_names, row))  
        for row in results]                                      #When I put in "results" it serialized the data. 
    return jsonify(data)


if __name__ == "__main__":
#    app.run(host='127.0.0.1')
    app.run(host='192.168.2.253')	
#    app.run(host='50.197.246.137')	
app.run()

#/api/v1/resources/HAII/all'
#http://127.0.0.1:5000/api/v1/resources/books/all 
#http://127.0.0.1:5000/api/v1/resources/books?author=Connie+Willis 
#http://127.0.0.1:5000/api/v1/resources/books?author=Connie+Willis&published=1999 
#http://127.0.0.1:5000/api/v1/resources/books?published=2010
#http://127.0.0.1:5000/api/v1/resources/HAII/all 
#http://127.0.0.1:5000/api/v1/resources/HAII?State=NC
#http://127.0.0.1:5000/api/v1/resources/HAII?author=Connie+Willis&published=1999 
#http://127.0.0.1:5000/api/v1/resources/HAII?published=2010