def get_consumer_complaints_counts():
    import os
import pandas as pd
import os
import codecs
import sys
import csv
import io
	
df = pd.read_csv('data/dictionary_Consumer_Complaints.csv', encoding='cp1258')

df.columns = ['Company_response', 'Product', 'State', 'Consumer_disputed', 'Timely_response', 'Issue', 'Company']
#df.columns = ['Company', 'Timely response?']

print(df)
##################################################
df1 = pd.crosstab( [df.Company], [df.Timely_response], margins=True) 

df4 = df1.div(df1["All"], axis=0)
'''
df2 = pd.crosstab( [df.Company], [df.Consumer_disputed], margins=True) 
df5 = df2.div(df2["All"], axis=0)
df3 = pd.crosstab( [df.Company], [df.Timely_response, df.Consumer_disputed], margins=True) 
df6 = df3.div(df3["All"], axis=0)
'''
##################################################
#writer = pd.ExcelWriter('data/Consumer_Complaints.xlsx', engine='xlsxwriter')
#writer = pd.ExcelWriter('C:/Users/drjef/OneDrive/AllData/Consumer_Finance/Consumer_Complaints.xlsx', engine='xlsxwriter')
writer = pd.ExcelWriter('D:/Users/drjef/OneDrive/AllData/OpenData/6-Consumer/6-1-20-13-CT_CC.xlsx', engine='xlsxwriter')

df1.to_excel(writer, sheet_name='Timely counts')
'''
df2.to_excel(writer, sheet_name='Disputed counts')
df3.to_excel(writer, sheet_name='Total counts')
'''
df4.to_excel(writer, sheet_name='Timely posteriors')
'''
df5.to_excel(writer, sheet_name='Disputed posts')
df6.to_excel(writer, sheet_name='Total posts')
'''
#########################INSTRUCTIONS############################

writer.save()
writer.close()


