# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 14:15:00 2018

@author: akansal2
"""

import numpy as np

a = np.array([1,2,3,4])
print(a)

import time
a = np.random.rand(10000000)
b = np.random.rand(10000000)
tic = time.time()
c= np.dot(a,b)
toc = time.time()
print('vectorization time is ' + str(1000*(toc-tic)) + 'ms' )


#for loop
c = 0
tic = time.time()
for i in range(10000000):
    c += a[i] + b[i]
toc = time.time()
print('loop time is ' + str(1000*(toc-tic)) + 'ms' )


#Other vectorization
a = np.array([1,2,3,-4])
np.abs(a)
np.exp(a)
np.log(a)
np.maximum(a,0)
a**2
1/a
a = np.random.rand(3,3)
b = np.random.rand(3,1)
a = np.array([[1,2],[1,3]])
b = np.array([[2,3]])
a*b