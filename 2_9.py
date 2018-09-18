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
x=coin(simlen)
n=np.random.normal(0,1,simlen)
a=4
lam=np.linspace(0,8,60)
err=[]
for i in range (0,60):
	y=a+n
	ind_r=np.nonzero(y<lam[i])
	err_n=2*np.size(ind_r)/simlen
	y=-a+n
	ind_r=np.nonzero(y>lam[i])
	err_2=2*np.size(ind_r)/simlen
	err.append((err_n+err_2)/2)

plt.plot(lam,err)
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.show()