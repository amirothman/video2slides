import numpy as np
import cv2
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

folder_name = sys.argv[1]
output_folder = sys.argv[2]
images = [ folder_name+'/'+file_name for file_name in os.listdir(folder_name)]

arr = []


for i in range(len(images)-1):
  pair = images[i:i+2]
  a = cv2.imread(pair[0])
  b = cv2.imread(pair[1])
  n = (np.linalg.norm(b-a))*10000/(a.shape[0]*a.shape[1])
  element = {'norm':n,'file_1':pair[0],'file_2':pair[1]}
  arr.append(element)

df = pd.DataFrame(arr)
seventy_five = df['norm'].describe()[6]

chosen = df[df['norm'] > df.norm.quantile(0.9)]

#http://stackoverflow.com/questions/11854847/display-an-image-from-a-file-in-an-ipython-notebook
print '#!/bin/bash'
for item in chosen['file_2'].iteritems():
  print('cp %(filename)s %(output_folder)s'%{'filename':item[1],'output_folder':output_folder})



