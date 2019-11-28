#import heads
import pandas as pd
from myChartfunctions import \
excel_header1, excel_header2, excel_header3, excel_header4, excel_header5, excel_header6, \
chart_series1, chart_series2, chart_series3, newid1

df = pd.read_csv(newid1)

print(df)
df1 = pd.DataFrame(df)
df1 = df.set_index('DATE', 'change')

from myChartfunctions import excel_file
from myChartfunctions import sheet_name

cols_to_convert = ['change']

for col in cols_to_convert: df1[col] = pd.to_numeric(df1[col], errors='coerce')

writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
df1.to_excel(writer, sheet_name=sheet_name)

workbook = writer.book
worksheet = writer.sheets[sheet_name]

chart = workbook.add_chart({'type': 'column'})

chart.add_series({'values':chart_series1,'gap': 2,})
chart.set_y_axis({'major_gridlines': {'visible': False}})

chart.set_legend({'position': 'none'})

############################################ START CHARTS #################################

# Create a Line chart.
chart1 = workbook.add_chart({'type': 'line'})

# Configure the second series with a moving average trendline.
chart1.add_series({
    'categories': chart_series2,
	'values': chart_series1,
    'trendline': {
    'type': 'polynomial',
    'order': 2,
    },
})

# Add a chart title.
chart1.set_title({'name': excel_header1})

# Insert the chart into the worksheet (with an offset).
worksheet.insert_chart('D2', chart1, {'x_offset': 500, 'y_offset': 0})
##############

# Create a Line chart.
chart1 = workbook.add_chart({'type': 'line'})

# Configure the second series with a moving average trendline.
chart1.add_series({
    'categories': chart_series2,
    'values': chart_series1,	
    'trendline': {'type': 'linear'},
})

# Add a chart title.
chart1.set_title({'name': excel_header2})

# Insert the chart into the worksheet (with an offset).
worksheet.insert_chart('D2', chart1, {'x_offset': 500, 'y_offset': 300})

#######################################NEW

# Create a Line chart.
chart1 = workbook.add_chart({'type': 'line'})

# Configure the second series with a moving average trendline.
chart1.add_series({
    'categories': chart_series2,
    'values': chart_series1,
})

# Add a chart title.
chart1.set_title({'name': excel_header3})

# Insert the chart into the worksheet (with an offset).
worksheet.insert_chart('D2', chart1, {'x_offset': 500, 'y_offset': 600})

############################################################################################
########################################### CHANGES#########################################
############################################################################################
df = pd.read_csv(newid1)

# Create a Line chart.
chart1 = workbook.add_chart({'type': 'line'})

# Configure the second series with a moving average trendline.
chart1.add_series({
    'categories': chart_series2,
    'values': chart_series3,
    'trendline': {
    'type': 'polynomial',
    'order': 2,
    },
})

# Add a chart title.
chart1.set_title({'name': excel_header4})

# Insert the chart into the worksheet (with an offset).
worksheet.insert_chart('D2', chart1, {'x_offset': 10, 'y_offset': 0})
##############

# Create a Line chart.
chart1 = workbook.add_chart({'type': 'line'})

# Configure the second series with a moving average trendline.
chart1.add_series({
    'categories': chart_series2,
    'values': chart_series3,
    'trendline': {'type': 'linear'},
})

# Add a chart title.
chart1.set_title({'name': excel_header5})

# Insert the chart into the worksheet (with an offset).
worksheet.insert_chart('D2', chart1, {'x_offset': 10, 'y_offset': 300})

#######################################NEW

# Create a Line chart.
chart1 = workbook.add_chart({'type': 'line'})

# Configure the second series with a moving average trendline.
chart1.add_series({
    'categories': chart_series2,
    'values': chart_series3,
})

# Add a chart title.
chart1.set_title({'name': excel_header6})

# Insert the chart into the worksheet (with an offset).
worksheet.insert_chart('D2', chart1, {'x_offset': 10, 'y_offset': 600})
#################################################

writer.save()
#########################################################WRITE TO FILE#################################

