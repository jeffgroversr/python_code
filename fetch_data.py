import pandas as pd
import os
from datetime import datetime

df = pd.read_csv("https://data.consumerfinance.gov/api/views/s6ew-h6mp/rows.csv?accessType=DOWNLOAD")

df.to_csv('data/Consumer_Complaints.csv')