import numpy as np
import mpmath as mp
import scipy
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess
from scipy.integrate import quad
import scipy.integrate as spint

simlen=10000
x=np.ones(simlen)
n=np.random.normal(0,1,simlen)
a=np.linspace(0,4,30)
err=[]
for i in range (0,30):
	y=a[i]*x+n
	ind_r=np.nonzero(y<0)
	err_n=np.size(ind_r)
	err.append(err_n/simlen)


plt.plot(a,err)
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.show()