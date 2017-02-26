# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 17:30:53 2017

@author: tom
"""

import os, shutil

def makeDirs(nr_of_dirs,destLoc):
    for i in range(nr_of_dirs):
        new_dir = os.path.join(destLoc,str(i))
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
            
def copyImg(oldLoc,newLoc):
    shutil.copy2(oldLoc,newLoc)

def getImages(folder):
    files = os.listdir(folder)
    imgList = [os.path.join(folder,filename) for filename in files if filename.endswith('.jpg')]
    return imgList