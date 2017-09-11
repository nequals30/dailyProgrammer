# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 06:43:33 2017

This is my first mini project using python (and spyder). This is almost definately
not the most efficient way to do this.

https://www.reddit.com/r/dailyprogrammer/comments/6wjscp/2017828_challenge_329_easy_nearest_lucky_numbers/

@author: nEquals30
"""

import numpy as np

def nearestLuckyNumber(num):
    # Initialize List
    nn = 1.2 * num # adding 20% margin to make sure next lucky number is captured. bad.
    myList = np.arange(nn) + 1
    
    # Start by deleting every second element (ptr=2)
    # We will need to have the ptr point to the 2nd element twice, once for 2 and 
    # once for 3.
    idxPtr = 2
    idxRm = np.arange(myList[idxPtr-1],nn+1,myList[idxPtr-1])
    myList = np.delete(myList,idxRm-1)
    
    # After that, we will keep incrementing ptr by 1
    while (idxPtr<myList.size):
        idxRm = np.arange(myList[idxPtr-1],nn+1,myList[idxPtr-1])
        myList = np.delete(myList,idxRm-1)
        idxPtr = idxPtr+1
    
    # Results
    if num in myList:
        print(str(num) + ' is a lucky number')
    else:
        lt = max(myList[myList<num])
        gt = min(myList[myList>num])
        print "%s < %s < %s " % (lt,num,gt)