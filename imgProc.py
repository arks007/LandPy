import cv2
import os
import math
import numpy as np
from matplotlib import pyplot as plt

np.seterr(divide='ignore', invalid='ignore')
np.seterr(over='ignore')

fileSuffixes = np.array(['band1.tif', 'band2.tif','band3.tif', 'band4.tif', 'band5.tif', 'band6.tif', 'band7.tif'])

#a function that crops and saves multiple .tif landsat band images 
def fldrRegSelFunc(name, source, destination, cropParams):
    i = 0
    for filename in os.listdir(source):
        if filename.endswith('.tif') and (i > 3) and (i < 10) :
            img = regionSelector(os.path.join(source, filename), cropParams[0], cropParams[1], cropParams[2], cropParams[3]) 
            cv2.imwrite(name + fileSuffixes[i], img)
        i = i + 1

#a function that crops a specific region from a raw landsat band images 
def regionSelector(img, x, y, dX, dY):
    rawImg = cv2.imread(img)
    img = rawImg[y:dY, x:dX]
    return img