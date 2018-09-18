import numpy as np
import scipy 
from mpl_toolkits.mplot3d import Axes3D
import mpmath as mp
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess

# fig=plt.figure()
# ax=fig.add_subplot(111,projection='3d')

simlen=int(1e5)
# X1 = np.random.normal(0,1,simlen)
# X2 = np.random.normal(0,1,simlen)
N1 = np.random.normal(0,1,simlen)
N2 = np.random.normal(0,1,simlen)
# A = np.sqrt(np.square(X1)+np.square(X2))
# A=4
gamma=np.linspace(1,10,20)
err=[]

for i in range(0,20):
	A=np.random.rayleigh(np.sqrt(gamma[i]/2),simlen)
	y0_1=A*1+N1
	y0_2=N2
	err_n=np.nonzero(y0_1<y0_2)
	err_size=np.size(err_n)
	err.append(err_size/100000.0)


plt.plot(gamma,err,"go")
# plt.plot(y0_1,y0_2,"go")
# plt.plot(y1_1,y1_2,"ro")

plt.show()