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
# x = np.linspace(-4,4,30)
# X1 = np.random.normal(0,1,simlen)
# X2 = np.random.normal(0,1,simlen)
N1 = np.random.normal(0,1,simlen)
N2 = np.random.normal(0,1,simlen)
gamma=np.linspace(1,10,20)
err = []
# err2 = []

for i in range(0,20):
	A=np.random.rayleigh(np.sqrt(gamma[i]/2),simlen)
	err_ind1 = np.nonzero(N2-N1>A)
	# err_ind2 = np.nonzero(N2<x[i])
	err_n1=np.size(err_ind1)
	# err_n2=np.size(err_ind2)
	err.append((err_n1)/simlen)
	# err2.append(err_n2/simlen)
err2=[]

for i in range(0,20):
	A=np.random.rayleigh(np.sqrt(gamma[i]/2),simlen)
	y0_1=A*1+N1
	y0_2=N2
	err_n=np.nonzero(y0_1<y0_2)
	err_size=np.size(err_n)
	err2.append(err_size/simlen)

plt.plot(gamma,err,"r")
plt.plot(gamma,err2,"go")

plt.legend(["theory","simulated"])
plt.xlabel("gamma")
plt.ylabel('$P_e$')

# plt.plot(N2-N1,"r")
# plt.plot(y0_1,y0_2,"go")
# plt.plot(y1_1,y1_2,"ro")

plt.show()