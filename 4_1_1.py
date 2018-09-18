import numpy as np
import mpmath as mp
import scipy 
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess

size=100000.0
x=np.linspace(-10.0,10.0,300.0)
x1=np.random.normal(0,1,size)
x2=np.random.normal(0,1,size)
y=x1**2 + x2**2
err=[]
cdf=[]
pdf=[]
for i in range(0,300):
	err_ind=np.nonzero( y<x[i] )
	err_n=np.size(err_ind)
	cdf.append(err_n/size)
    
for i in range(0,299):
	test=(cdf[i+1]-cdf[i])/(x[i+1]-x[i])
	pdf.append(test)
    

plt.plot(x[0:299],pdf,'r-')
plt.plot(x,cdf,'g-')
plt.show()