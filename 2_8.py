import numpy as np
import mpmath as mp
import scipy
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess
from scipy.integrate import quad
import scipy.integrate as spint

simlen=10000
x=1
n=np.random.normal(0,1,simlen)
a=np.linspace(1,np.sqrt(10),20)
err=[]
for i in range (0,20):
	ind_r=np.nonzero(-n>a[i])
	err_n=np.size(ind_r)
	err.append(err_n/simlen)

plt.semilogy(a,scipy.special.erfc(a/np.sqrt(2))/2,'ro')	
plt.semilogy(a,err)
plt.grid()
plt.xlabel('$SNR$')
plt.ylabel('$F_X(x)$')
plt.show()