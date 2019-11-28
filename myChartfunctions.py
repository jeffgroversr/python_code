###############################ARIMA_prep.py################################
import pandas as pd

newid1 = "data/%AAAFF.csv"
#newid = "data/AAAFF.csv"
#excel_file = 'C:/Users/drjef/OneDrive/ARIMAs/FRED Series/Daily/Bond Series/plot_AAAFF_Change.xlsx'
excel_file = 'D:/Users/drjef/OneDrive/AllData/OpenData/11-Finance/11-1-20-13-plot_AAAFF_Change.xlsx'
sheet_name = 'AAAFF'

newid1 = 'data/%AAAFF.csv'
newid2 = 'data/%AAAFF_head.csv'
change = 'AAAFF'

chart_series1 = '=AAAFF!$C$2:$C$300'
chart_series2 = '=AAAFF!$A$2:$A$300'
chart_series3 = '=AAAFF!$B$2:$B$300'

SA_TrendlinePercent = "Moody's Seasoned Aaa Corporate Bond Minus Federal Funds Rate (AAAFF), Not Seasonally Adjusted, Daily | % Change (1-Year Ago)| SA Trendline."
SA_Trendline = 'Mexico / U.S. Foreign Exchange Rate, Not Seasonally Adjusted, Daily | SA Trendline.'

excel_header1 = SA_TrendlinePercent
excel_header2 = SA_TrendlinePercent
excel_header3 = SA_TrendlinePercent
excel_header4 = SA_Trendline
excel_header5 = SA_Trendline
excel_header6 = SA_Trendline

newsummary1 = "'#PoT | #ARIMA| #FREDSeries | #Bond | Check this out! We have just calculated today's FRED Bond Series Moody's Seasoned Aaa Corporate Bond Minus Federal Funds Rate (AAAFF), Not Seasonally Adjusted| (Microsoft Excel Charts) @ http://bit.ly/2KWVxOR #{}'"
newsummary2 = "FRED Bond Moody's Seasoned Aaa Corporate Bond Minus Federal Funds Rate (AAAFF), Not Seasonally Adjusted | (Microsoft Excel Charts)"