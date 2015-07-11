import numpy as np
import cv2
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

folder_name = sys.argv[1]
output_folder = sys.argv[2]
#folder_name = 'tmp-ffmpeg-folder'
#output_folder = 'tmp-output-folder'
images = [ folder_name+'/'+file_name for file_name in os.listdir(folder_name)]

arr = []


for i in range(len(images)-1):
  pair = images[i:i+2]
  a = cv2.imread(pair[0])
  b = cv2.imread(pair[1])
  n = (np.linalg.norm(b-a))*10000/(a.shape[0]*a.shape[1])
  sys.stdout.write('.')
  element = {'norm':n,'file_1':pair[0],'file_2':pair[1]}
  arr.append(element)

df = pd.DataFrame(arr)

chosen = df[df['norm'] > df.norm.quantile(0.95)]
# 
# quantile_var = 0.9
# 
# 
# while chosen.size > 200:
#   quantile_var = quantile_var + 0.05
#   chosen = df[df['norm'] > df.norm.quantile(quantile_var)]
# 

script = open('script_for_copying.sh','w')
script.write('#!/bin/bash\n')

for item in chosen['file_2'].iteritems():
  script.write('cp %(filename)s %(output_folder)s \n'%{'filename':item[1],'output_folder':output_folder})

# print '#!/bin/bash'
# for item in chosen['file_2'].iteritems():
#   print('cp %(filename)s %(output_folder)s'%{'filename':item[1],'output_folder':output_folder})



