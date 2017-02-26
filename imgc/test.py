# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 16:14:28 2017

@author: tom
"""

import imgclus
import imgfolder
import imgavg
import imgsub
import os

#Load Images
fileLoc = 'C:\\Users\\tom\\Documents\\School\\Master_Data_Science\\mlip\\data\\train\\*\\*.jpg'
images = imgclus.loadNImages(50,fileLoc)
train = imgclus.readImages(images)
train = imgclus.resizeImages(train)

#Cluster Images
y = imgclus.computeDistances(train)
clusters = imgclus.getClusters(y,images)

#Cluster Images on Size
#clusters = imgclus.getSizeClusters(images)

#Output Clusters
destLoc = 'C:\\Users\\tom\\Documents\\School\\Master_Data_Science\\mlip\\clusters' 
currentLoc = 'C:\\Users\\tom\\Documents\\School\\Master_Data_Science\\mlip'
imgfolder.makeDirs(len(clusters),destLoc)
for i, c in enumerate(clusters):
    for img in c:
        imgLoc = img
        oldLoc = imgLoc
        newLoc = os.path.join(destLoc,str(i))
        imgfolder.copyImg(oldLoc,newLoc)
       
#Average Clusters
averages = []
for i in range(len(clusters)):
    clusterLoc = 'C:\\Users\\tom\\Documents\\School\\Master_Data_Science\\mlip\\clusters\\%s'%(i)
    outputLoc = "C:\\Users\\tom\\Documents\\School\\Master_Data_Science\\mlip\\averages\\Average%s.jpg"%(i)
    averages.append(outputLoc)
    imgavg.computeAverageImg(clusterLoc,outputLoc)   
  
#Subtracting Average from Original Images
destLoc = 'C:\\Users\\tom\\Documents\\School\\Master_Data_Science\\mlip\\subtracted'
imgfolder.makeDirs(len(clusters),destLoc)
for i in range(len(clusters)):
    clusterLoc = 'C:\\Users\\tom\\Documents\\School\\Master_Data_Science\\mlip\\clusters\\%s'%(i)
    clusterImgList = imgfolder.getImages(clusterLoc)
    averageImg = averages[i]
    outputfile = "%s\\%s\\subtracted"%(destLoc,i)
    for index, img in enumerate(clusterImgList):
        imgsub.subtractImg(img,averageImg,"%s%s.jpg"%(outputfile,index))