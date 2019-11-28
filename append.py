#https://towardsdatascience.com/merging-spreadsheets-with-python-append-f6de2d02e3f3
from datetime import datetime
dateTimeObj = datetime.now()
print(dateTimeObj)
mytime = (dateTimeObj)
'''
import shutil
############################################################
shutil1 = "D:/Users/drjef/OneDrive/AllData/OpenData/4-BusinessUSA/4-2-20-1-FBO.xlsx"
shutil2 = "D:/Users/drjef/OneDrive/AllData/OpenData/4-BusinessUSA/archive/current_fbo.xlsx"
############################################################
shutil.copy(shutil1, shutil2)
'''

import pandas as pd

# Read all three files into pandas dataframes
current_fbo = pd.read_excel("D:/Users/drjef/OneDrive/AllData/OpenData/4-BusinessUSA/4-2-20-1-FBO.xlsx")
master_fbo = pd.read_excel("D:/Users/drjef/OneDrive/AllData/OpenData/4-BusinessUSA/master_fbo.xlsx")

# Create a list of the files in order you want them appended
all_df_list = [current_fbo, master_fbo]

# Merge all the dataframes in all_df_list
# Pandas will automatically append based on similar column names
appended_df = pd.concat(all_df_list)

# Write the appended dataframe to an excel file
# Add index=False parameter to not include row numbers
appended_df.to_excel("D:/Users/drjef/OneDrive/AllData/OpenData/4-BusinessUSA/master_fbo.xlsx", index=False)