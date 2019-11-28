import pandas as pd
import numpy as np
from fetch_data import new_loc_1, new_loc_2

df = pd.read_csv(new_loc_1, encoding='utf-8') 

df1 = df[['PK','CCR','AGE','GENDER','RACE','ARRESTTIME','ARRESTLOCATION','OFFENSES','INCIDENTLOCATION','INCIDENTNEIGHBORHOOD','INCIDENTZONE','INCIDENTTRACT','COUNCIL_DISTRICT','PUBLIC_WORKS_DIVISION','X','Y']]
df1.rename(columns={'ARRESTTIME': 'TIME','INCIDENTZONE': 'ZONE', 'INCIDENTNEIGHBORHOOD': 'NEIGHBORHOOD','INCIDENTLOCATION':'LOCATION'}, inplace=True)

df1['reference'] = 'Arrest_data'
df2 = pd.DataFrame(df1, columns = ['reference', 'PK','CCR','AGE','GENDER','RACE','TIME','ARRESTLOCATION','OFFENSES','LOCATION','NEIGHBORHOOD','ZONE','INCIDENTTRACT','COUNCIL_DISTRICT','PUBLIC_WORKS_DIVISION','X','Y'])
df2.to_csv(read_loc_1)
				
###
df3 = pd.read_csv(new_loc_2, encoding='utf-8') 

df4 = df3[['PK','CCR','AGE','GENDER','RACE','CITEDTIME','INCIDENTLOCATION','OFFENSES','NEIGHBORHOOD','ZONE','INCIDENTTRACT','COUNCIL_DISTRICT','PUBLIC_WORKS_DIVISION','X','Y']]
df4.rename(columns={'CITEDTIME': 'TIME','INCIDENTLOCATION':'LOCATION'}, inplace=True)

df4['reference'] = 'non_traffic_citations'
df5 = pd.DataFrame(df4, columns = ['reference','PK','CCR','AGE','GENDER','RACE','TIME','LOCATION','OFFENSES','NEIGHBORHOOD','ZONE','INCIDENTTRACT','COUNCIL_DISTRICT','PUBLIC_WORKS_DIVISION','X','Y'])
df5.to_csv(read_loc_2)
##

df6 = pd.concat([df2, df5], sort=True)
print(df6)
df6.to_csv(read_join)







