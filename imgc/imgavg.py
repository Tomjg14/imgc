# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 17:30:19 2017

@author: tom
"""

import os
from PIL import Image
import numpy as np

def computeAverageImg(folder,destination):
    clusterImages = os.listdir(folder)
    imgList = [os.path.join(folder,filename) for filename in clusterImages if filename.endswith('.jpg')]
    w,h = Image.open(imgList[0]).size
    N = len(imgList)
    arr = np.zeros((h,w,3),np.float)
    
    for img in imgList:
        imgarr = np.array(Image.open(img),dtype=np.float)
        arr = arr+imgarr/N
    
    arr = np.array(np.round(arr),dtype=np.uint8)
    
    out = Image.fromarray(arr,mode="RGB")
    out.save(destination,"JPEG")
    #out.show()