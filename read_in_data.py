import pandas as pd

df = pd.read_csv('data/Consumer_Complaints.csv', encoding='utf-8') #, dtype={'Ward': str, 'Beat': str, 'District': str, 'Community Area': str})

#print(df)

df1 = df[['Date received', 'Product', 'Sub-product', 'Sub-issue', 'Consumer complaint narrative', 'Company public response', 'Company', 'State', 'ZIP code', 'Tags', 'Consumer consent provided?', 'Submitted via', 'Date sent to company', 'Company response to consumer', 'Timely response?', 'Consumer disputed?', 'Complaint ID']] 
print(df1)

df1.to_csv('data/read_Consumer_Complaints.csv')




