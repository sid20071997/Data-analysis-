import numpy as np
import mpmath as mp
import scipy
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess
from scipy.integrate import quad
import scipy.integrate as spint

maxrang=50
maxlim=6.0
x=np.linspace(-maxlim,maxlim,maxrange)
err=[]
pdf=[]
h=2*maxlim/(maxrange-1)
n=np.random.normal(0,1,simlen)
for i in range(0,maxrange):
	err_ind=np.nonzero(n<x[i])
	err_n=np.size(err_ind)
	err.append(err_n/simlen)

for i in range(0,axrange-1):
	test=(err[i+1]-err[i])/x[i+1]-x[i]
	pdf.append(test)

def guass_pdf(x):
	return 1/np.sqrt(2*np.pi)*np.exp(-x**2/2.0)

vec_guass_pdf=numpy.vectorize(guass.pdf)

plt.plot(x[0:(maxrange-1)].T,pdf(x))
plt.plot(x,vec_guass_pdf(x))
plot.grid()
plot.xlabel