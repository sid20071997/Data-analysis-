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
v=[]
err=[]
mxrange=1000
x=np.linspace(-10.0,10.0,mxrange)

v=np.sqrt(np.multiply(-2,np.log(np.subtract(1,arr))))

for i in range(0,mxrange):
	err_ind=np.nonzero(v<x[i])
	err_n=np.size(err_ind)
	err.append(err_n/size)
	
plt.plot(x,err)	
plt.show()