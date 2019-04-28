import cv2
import os
import math
import numpy as np
import csv
from matplotlib import pyplot as plt

np.seterr(divide='ignore', invalid='ignore')
np.seterr(over='ignore')


def binaryImgGen(imgType, source, destination):
    numerics = []
    i = 0
    for img in source:
        rawImg = cv2.imread(img, 0)
        if(imgType == 'ndvi'):
            ret, binImg = cv2.threshold(rawImg, .35, 1, cv2.THRESH_BINARY)
        else:
            ret, binImg = cv2.threshold(rawImg, 0, 1, cv2.THRESH_BINARY)
        cv2.imshow("bin img", binImg)
        cv2.imwrite(destination + '/binImg_' + str(i) +'.tif', binImg)
        numerics.append(extractSurfaceData(binImg))
    np.savetxt(destination + imgType + '.csv', numerics, delimiter=",", fmt='%s')
        
def extractSurfaceData(binImg):
    sum = 0
    for row in binImg:
        for pixel in row:
            if(pixel > 0):
                sum = sum + 1
    return sum


