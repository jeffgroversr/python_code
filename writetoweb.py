import pandas as pd
import csv
import xlsxwriter

df = pd.read_csv('data/FRED_Daily_Pop_Series_results.csv')
df.columns = ['No.', 'DATE','DAAA','DBAA','DCOILWTICO','DEXUSEU','DFII10','DFII5','DGS1','DGS10','DGS3MO','DGS5']  
print(df)

writer = pd.ExcelWriter('D:/Users/drjef/OneDrive/PythonCode/ActiveCode/UseCases/OpenData/11-Finance/YieldCurves/CorporateYieldCurves/data/FRED_Daily_Pop_Series_results.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='FRED Series', index=False)
writer.save()
writer.close()

import shutil
shutil1 = 'D:/Users/drjef/OneDrive/PythonCode/ActiveCode/UseCases/OpenData/11-Finance/FRED-Pop/data/FRED_Daily_Pop_Series_results.csv'
shutil2 = "D:/Users/drjef/OneDrive/AllData/OpenData/11-Finance/11-1-20-13-FRED_Daily_Pop_Series_results.csv"
shutil.copy(shutil1, shutil2)
