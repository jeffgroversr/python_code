import codecs
import csv
import pandas as pd

def percConvert(ser): return ser/float(ser[2])

with codecs.open("data/read_Consumer_Complaints.csv", 'r', encoding="cp1252", errors="surrogateescape") as csv_file:

    csv_reader = csv.DictReader(csv_file)

    with open('data/dictionary_Consumer_Complaints.csv', 'w') as dictionary_Consumer_Complaints:
        fieldnames=['Company response to consumer', 'Product', 'State', 'Consumer disputed?', 'Timely response?', 'Issue', 'Company']

        csv_writer = csv.DictWriter(dictionary_Consumer_Complaints, fieldnames=fieldnames, delimiter=',') 
        
        csv_writer.writeheader()
        
        for line in csv_reader:
        	del line['']
        	del line['Date received']
	        del line['Sub-product']
	        del line['Sub-issue']
	        del line['Consumer complaint narrative']
	        del line['Company public response']
	        del line['ZIP code']
	        del line['Tags']
	        del line['Consumer consent provided?']
	        del line['Submitted via']
	        del line['Date sent to company']
	        del line['Complaint ID']

	        csv_writer.writerow(line)
			
df = pd.read_csv('data/dictionary_Consumer_Complaints.csv')
print(df)


