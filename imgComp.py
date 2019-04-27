import cv2
import os
import math
import numpy as np
from matplotlib import pyplot as plt

np.seterr(divide='ignore', invalid='ignore')
np.seterr(over='ignore')

#functions to create composite images for analysis

#creates a Normalized Difference Vegetation Index(NDVI) composite 
#pixel values will range between -1 and 1
def createNDVIComp(path):
    for filename in os.listdir(path):
        if filename.endswith('band5.tif'):
            nir = cv2.imread(os.path.join(path, filename), 0)
        if filename.endswith('band4.tif'):
            red = cv2.imread(os.path.join(path, filename), 0)
    numerator = (np.int_(nir) - np.int_(red))
    denominator = (np.int_(nir) + np.int_(red))
    return (numerator/denominator)

#creates a Normalized Difference Water Index(NDWI) composite 
#pixel values will range between -1 and 1
def createNDWIComp(path):
    for filename in os.listdir(path):
        if filename.endswith('band5.tif'):
            nir = cv2.imread(os.path.join(path, filename), 0)
        if filename.endswith('band3.tif'):
            green = cv2.imread(os.path.join(path, filename), 0)
    numerator = (np.int_(green) - np.int_(nir))
    denominator = (np.int_(nir) + np.int_(green))
    return (numerator/denominator)

