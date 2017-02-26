# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 17:40:43 2017

@author: tom
"""

import cv2

def subtractImg(img1Loc,img2Loc,outputLoc):
    img1 = cv2.imread(img1Loc)
    img2 = cv2.imread(img2Loc)
    outputImg = cv2.subtract(img1,img2)
    cv2.imwrite(outputLoc,outputImg)