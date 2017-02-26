# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 15:44:13 2017

@author: tom
"""

import numpy as np
import pandas as pd
import sklearn import cluster
import random
import glob
import cv2

def loadImages(folder):
    imageFiles = sorted(glob.glob(folder), key=lambda x: random.random())
    return imageFiles

def loadNImages(n,folder):
    imageFiles = sorted(glob.glob(folder), key=lambda x: random.random())[:n]
    return imageFiles    

def resizeImages(images):
    return [cv2.resize(img, (224,224), cv2.INTER_LINEAR) for img in images]
    
def compare(args):
    img, img2 = args
    img = (img - img.mean()) / img.std()
    img2 = (img2 - img2.mean()) / img2.std()
    return np.mean(np.abs(img - img2))

def getSizeClusters(images):
    clusters = []
    shapes = np.array([str(img.shape) for img in images])
    for uniq in pd.Series(shapes).unique():
        cluster = np.array(images)[shapes == uniq]
        clusters.append(cluster)
    return clusters
    
def getClusters(y,images):
    clusters = []
    for uniq in pd.Series(y).value_counts().index:
        if uniq != -1:
            cluster = np.array(images)[y == uniq]
            clusters.append(cluster)
    return clusters
    
def computeDistances(images):
    distances = np.zeros((len(images), len(images)))
    for i, img in enumerate(images):
        all_imgs = [(img,img2) for img2 in images]
        dists = map(compare, all_imgs)
        distances[i, :] = dists
    cls = cluster.DBSCAN(metric='precomputed', min_samples=5, eps=0.6)
    y = cls.fit_predict(distances)
    return y
