#Directions:
#1. replace ID
#2. Replace shutil5 folder name with new ID inside the Charts folder
######################################       BEGIN        ######################################
import pandas as pd
######################################   fetch_data.py    #################################
idchange = 'AAAFF'
newid = 'data/AAAFF.csv'
######################################   ARIMA_prep.py    #################################
newid1 = 'data/%AAAFF.csv'
newid2 = 'data/%AAAFF_head.csv'
###################################### ARIMA_no_charts.py #####################
from pandas import read_csv
newsummary = "Moody's Seasoned Aaa Corporate Bond Minus Federal Funds Rate (AAAFF) | Percent | Not Seasonally Adjusted | Daily | (ARIMA Report)"
mywith = "data/%AAAFF_arima.txt"

import shutil
shutil1 = "data/%AAAFF_arima.txt"
#shutil2 = "C:/Users/drjef/OneDrive/ARIMAs/FRED Series/Daily/Bond Series/%AAAFF_arima.txt"
#shutil2 = "D:/Users/drjef/OneDrive/PythonCode/ActiveCode/UseCases/OpenData/ARIMAs/FRED Series/Bond Series/AAAFF_ARIMA/data/%AAAFF_arima.txt"
#shutil2 = "D:/Users/drjef/OneDrive/AllData/OpenData/11-Finance/%AAAFF_arima.txt"
shutil2 = "D:/Users/drjef/OneDrive/AllData/OpenData/11-Finance/11-1-20-13-%AAAFF_arima.txt"

#shutil3 = "C:/Users/drjef/venv/sedm/UseCases/Economics/ARIMAs/FRED Series/Bond Series/SummaryReports/%AAAFF_arima.txt"
#shutil3 = "D:/Users/drjef/OneDrive/PythonCode/ActiveCode/UseCases/OpenData/ARIMAs/FRED Series/Bond Series/SummaryReports/%AAAFF_arima.txt"
#shutil3 = "D:/Users/drjef/OneDrive/PythonCode/ActiveCode/UseCases/OpenData/11-Finance/ARIMAs/FRED Series/Bond Series/SummaryReports/%AAAFF_arima.txt"
shutil3 = "D:/Users/drjef/OneDrive/PythonCode/ActiveCode/UseCases/OpenData/11-Finance/ARIMAs/AAAFF/SummaryReports/%AAAFF.txt"

shutil4 = "data/%AAAFF.csv"
#shutil5 = "C:/Users/drjef/venv/sedm/UseCases/Economics/ARIMAs/FRED Series/Bond Series/AAAFF_ARIMA/AAAFF_Charts/data/%AAAFF.csv"
#shutil5 = "D:/Users/drjef/OneDrive/PythonCode/ActiveCode/UseCases/OpenData/ARIMAs/FRED Series/Bond Series/AAAFF_ARIMA/AAAFF_Charts/data/%AAAFF.csv"
#shutil5 = "D:/Users/drjef/OneDrive/PythonCode/ActiveCode/UseCases/OpenData/11-Finance/ARIMAs/FRED Series/Bond Series/AAAFF_ARIMA/AAAFF_Charts/data/%AAAFF.csv"
shutil5 = "D:/Users/drjef/OneDrive/PythonCode/ActiveCode/UseCases/OpenData/11-Finance/ARIMAs/AAAFF/AAAFF_Charts/%AAAFF.csv"

#####################################      run.py         ##########################################
newsummary1 = "'#PoT | #ARIMA| #FREDSeries | #BOND | Check this out! We have just calculated today's FRED Bond Series Moody's Seasoned Aaa Corporate Bond Minus Federal Funds Rate (AAAFF) | (ARIMA Report) @ http://bit.ly/2KWVxOR #{}'"
newsummary2 = "Percent, Not Seasonally Adjusted | (ARIMA Report)"