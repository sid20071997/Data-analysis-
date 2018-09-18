from __future__ import division
import numpy as np
import mpmath as mp
import scipy 
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess
import math

arr=np.loadtxt('s.dat',dtype=float)

size=1000000
mxrange=100
def guass_pdf(x):
	return 1/np.sqrt(2*np.pi)*np.exp(-x**2/2.0)
err=[]
x=np.linspace(-6,6,mxrange)
pdf=[]
for i in range(0,mxrange):
	err_ind=np.nonzero(arr<x[i])
	err_n=np.size(err_ind)
	err.append(err_n/size)

for i in range(0,mxrange-1):
	test=(err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test)

vec_gauss_pdf=np.vectorize(gauss_pdf)
	
plt.plot(x[0:mxrange-1],pdf,'r')
plt.plot(x,vec_guass_pdf(x),'bo')
plt.show()