#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 10:54:55 2018

@author: chandrasendr
"""

import numpy as np
import time
import sys
#
#
#a = np.array([1,2,3,4])
#
#print(a[0])
#
## Advanges of numpy
## 1. Comparison of numpy array and python array interms of memory usage
#l = range(1000)
#print(sys.getsizeof(1)*len(l))
#
#array = np.arange(1000)
#print(array.size*array.itemsize)
#
## 2. Comparision of numpy array processsing and python list processing
#size = 1000000
#
#l1 = range(size)
#l2 = range(size)
#
#a1 = np.arange(size)
#a2 = np.arange(size)
#
## python list
#start = time.time()
#result = [(x + y) for x, y in zip(l1, l2)]
#print("Python list took: ",(time.time()-start)*1000)
#
## numpy array
#start = time.time()
#result = a1 + a2
#print("numpy took: ", (time.time()-start)*1000)
#
#a = np.array([[1,2],[3,4],[5,6]])
#print(a.ndim)
#print(a.itemsize)
#print(a.dtype)
#
#
#a1 = np.array([[1,2],[3,4],[5,6]], dtype=np.complex)
#print(a1.ndim)
#print(a1.itemsize)
#print(a1.dtype)
#print(a1.size)
#print(a1)
#print(a1.shape)
#
#print(np.zeros((3,4)))
#print(np.ones((3,4)))
#
#print(range(1,5))
#print(np.arange(1,5))
#print(np.arange(1,5,2))
#
#print(np.linspace(1,5,10))
#
#
#a = np.array([[1,2],[3,4],[5,6]])
#print(a.shape)
#print(a.reshape(2,3))
#print(a.ravel())

## Mathamatical operations in numpy
#a = np.array([[1,2],[3,4],[5,6]])
#print(a)
#print(a.sum(axis=0))
#print(a.sum(axis=1))
#print(np.sqrt(a))
#print(np.std(a))

#a = np.array([[1,2],[3,4]])
#b = np.array([[5,6],[7,8]])
#
#print(a+b)
#print(a*b)
#print(a.dot(b))

# Indexing and slicing using numpy
#n = [6,7,8]
#print(n[0:2])
#print(n[-1])
#
#a = np.array([6,7,8])
#print(a[0:2])

#a = np.array([[1,2,7],[3,4,8],[5,6,9]])
#print(a)
#print(a[1,2])
#print(a[0:2, 2])
#print(a[-1,0:2])
## printing last two columns
#print(a[:, 1:3])

#for row in a:
#    print(row)
## Flattning the array
#for cell in a.flat:
#    print(cell)
#
#a = np.arange(6).reshape(3,2)
#b = np.arange(6,12).reshape(3,2)
#print(a)
#print(b)
## Stacking vertically
#print(np.vstack((a,b)))
## Stacking horizontally
#print(np.hstack((a,b)))
#
#a = np.arange(30).reshape(2,15)
#print(a)
## Spliting the array horizontally
#result = np.hsplit(a,3)
#print(result[0])
#
## Spliting the array vertically
#result = np.vsplit(a,2)
#print(result[0])
#
## Indexing using boolean array
#a = np.arange(12).reshape(3,4)
#print(a)
#
#b = a > 4
#print(b)
#
## This prints all the elements in the array which stisfies the b condition
#print(a[b])
#
#a[b] = -1
#print(a)

# Iterate numpy array using nditer
#a = np.arange(12).reshape(3,4)
#
#print(a)
## prints all the elements in the array
#for row in a:
#    print(row)
## prints individual elements 
#for row in a:
#    for cell in row:
#        print(cell)
## extra for loop can be skipped by using flatten method on array
#for cell in a.flatten():
#    print(cell)
#    
## nditer in C order which is column wise
#for x in np.nditer(a, order='C'):
#    print(x)   
#    
## nditer in F (Fortran) order which is row wise
#for x in np.nditer(a, order='F'):
#    print(x)  
#        
#for x in np.nditer(a, order='F',flags=['external_loop']):
#    print(x)  
#        
## squaring an array using nditer
#for x in np.nditer(a, op_flags=['readwrite']):
#    x[...]=x*x
#print(a)
#
#b = np.arange(3,15,4).reshape(3,1)
#print(b)
#
## iterrating through two arrays simultaniously
#for x,y in np.nditer([a,b]):
#    print(x,y)






















