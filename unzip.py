import zipfile
import os
with zipfile.ZipFile("daily_44201_2018.zip","r") as zip_ref:
    zip_ref.extractall("flatfile")

os.remove('daily_44201_2018.zip')
