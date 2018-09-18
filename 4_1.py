from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import mpmath as mp
import scipy
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess
from scipy.integrate import quad
import scipy.integrate as spint

x=1
simlen=100000
err=[]
err1=[]
x1=np.random.normal(0,1,simlen)
x2=np.random.normal(0,1,simlen)
n=np.random.normal(0,1,simlen)
gamma=np.linspace(0,10,20)
for i in range(0,20):
	p=np.sqrt(gamma[i]/2)*np.sqrt(x1**2+x2**2)
	y=p+n
	ind_r=np.nonzero(y<0)
	err_n=np.size(ind_r)/simlen
	err.append(err_n)
for i in range(0,20):
	p=np.random.rayleigh(np.sqrt(gamma[i]/2),simlen)+n
	ind_r=np.nonzero(p<0)
	err1_n=np.size(ind_r)/simlen
	err1.append(err1_n)

plt.semilogy(gamma,err)
plt.semilogy(gamma,err1,'ro')
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.show()






