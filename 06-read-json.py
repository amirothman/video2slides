import json
import os
import sys

folder_name = sys.argv[1]

for idx,file_name in enumerate(os.listdir(folder_name)):
  f = open(folder_name+'/'+file_name)
  arr = json.load(f)
  for element in arr:
    (idx,element) 
