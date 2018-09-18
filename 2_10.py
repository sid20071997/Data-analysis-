import numpy as np
import mpmath as mp
import scipy
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess
from scipy.integrate import quad
import scipy.integrate as spint

def coin(x):
	return 2*np.random.randint(2,size=x)-1

simlen=10000
x=1
n=np.random.normal(0,1,simlen)
a=4
lam=np.linspace(-15,15,100)
err1=[]
pdf1=[]
err2=[]
pdf2=[]
y=a+n
for i in range (0,100):
	ind_r=np.nonzero(y<lam[i])
	err_n=np.size(ind_r)
	err1.append(err_n)
for i in range (0,99):
	test=(err1[i+1]-err1[i])/(lam[i+1]-lam[i])
	pdf1.append(test)


x=-1
y=-a+n
for i in range (0,100):
	ind_r=np.nonzero(y<lam[i])
	err_n=np.size(ind_r)
	err2.append(err_n)
for i in range (0,99):
	test=(err2[i+1]-err2[i])/(lam[i+1]-lam[i])
	pdf2.append(test)


plt.plot(lam[0:99],pdf1)
plt.plot(lam[0:99],pdf2)
plt.grid()
plt.xlabel('$lam$')
plt.ylabel('$F_X(x)$')
plt.show()