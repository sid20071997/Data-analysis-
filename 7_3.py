from __future__ import division
import numpy as np
import mpmath as mp
import scipy 
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess
import math

arr=np.loadtxt('uni.dat',dtype=float)

size=1000000
mxrange=1000

err=[]
x=np.linspace(0.0,1.0,mxrange)
pdf=[]
for i in range(0,mxrange):
	err_ind=np.nonzero(arr<x[i])
	err_n=np.size(err_ind)
	err.append(err_n/size)

test=0.0
for i in range(0,mxrange-1):
	test=(err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test)

err2=[]
for i in range(0,mxrange-1):
	err2.append(x[i])
	
plt.plot(x[0:mxrange-1],pdf,'ro')
plt.plot(x[0:mxrange-1],err2,'bo')
plt.plot(x,err)
plt.show()