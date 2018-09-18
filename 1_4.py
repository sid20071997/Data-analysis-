import numpy as np
import mpmath as mp
import scipy
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess
from scipy.integrate import quad
import scipy.integrate as spint

x=np.linspace(-4,4,30)
simlen=100000
err=[]
n=np.random.normal(0,1,simlen)
for i in range(0,30):
	err_ind=np.nonzero(n <x [i])
	err_n=np.size(err_ind)
	err.append(err_n/simlen)

plt.plot(x.T,err)
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.show()