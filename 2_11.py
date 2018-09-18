import numpy as np
import mpmath as mp
import scipy
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess
from scipy.integrate import quad
import scipy.integrate as spint




simlen=10000
x=np.linspace(-10,10,simlen)
a=np.linspace(-10,10,5)


for i in range (0,5):
	err=[]
	for j in range (0,simlen-1):
		p=1/np.sqrt(2*np.pi)*np.exp(-(x[j]-a[i])**2/2)
		err.append(p)
	plt.plot(x[0:9999],err)
	plt.grid()
plt.show()


