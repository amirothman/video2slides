import numpy as np
import cv2
import os
import pandas as pd

folder_name = 'split-sample-vid'

images = [ folder_name+'/'+file_name for file_name in os.listdir(folder_name)]

arr = []

for i in range(len(images)-1):
  pair = images[i:i+2]
  a = cv2.imread(pair[0])
  b = cv2.imread(pair[1])
  # a_th = cv2.adaptiveThreshold(a,1,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
  # b_th = cv2.adaptiveThreshold(b,1,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
  n = (np.linalg.norm(b-a))*10000/(a.shape[0]*a.shape[1])
  arr.append(n)
  print('%(a)s,%(b)s,%(c)s' % {'a':n,'b':pair[0],'c':pair[1]})
