import glob
import os
filelist=glob.glob("C:/Users/drjef/venv/sedm/UseCases/Economics/CT_Insurance/data/*")
for file in filelist:
  os.remove(file)