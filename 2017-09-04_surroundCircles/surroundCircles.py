# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 14:08:09 2017

Easy challenge, draw a bounding box around a set of circles.
Harder challenge, allow the bounding box to rotate [not yet implemented]

https://www.reddit.com/r/dailyprogrammer/comments/6y19v2/20170904_challenge_330_easy_surround_the_circles/

@author: boss
"""

import numpy as np

def bbox(x_coord,y_coord,radii):
    # Calculates Bounding Box
    xmin = min(x_coord-radii)
    xmax = max(x_coord+radii)
    ymin = min(y_coord-radii)
    ymax = max(y_coord+radii)
    return(xmin,xmax,ymin,ymax)

def rotate(radians):
    # NOT IMPLEMENTED


# [X, Y, Radius]
testIn = np.array([[1, 1, 2],
                   [2, 2, 0.5],
                   [-1,-3,2],
                   [5 ,2 ,1]])
(xmin,xmax,ymin,ymax) = bbox(testIn[:,0],testIn[:,1],testIn[:,2])
bboxArea = (xmax-xmin)*(ymax-ymin)

# Print Final Bounding Box
print(str(xmin)+","+str(ymin))
print(str(xmin)+","+str(ymax))
print(str(xmax)+","+str(ymin))
print(str(xmax)+","+str(ymax))