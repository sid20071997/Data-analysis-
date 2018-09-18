import numpy as np
import scipy 
from mpl_toolkits.mplot3d import Axes3D
import mpmath as mp
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

simlen=int(1e3)
X1 = np.random.normal(0,1,simlen)
X2 = np.random.normal(0,1,simlen)
N1 = np.random.normal(0,1,simlen)
N2 = np.random.normal(0,1,simlen)
A = np.sqrt(np.square(X1)+np.square(X2))
# A=4
gamma=np.linspace(1,10,20)
err=[]
err2=[]
y0_1=A*1+N1
y0_2=A*0+N2

y1_1=A*0+N1
y1_2=A*1+N2

ax.scatter(np.arange(0,simlen,1),y0_1,y0_2,"ro")
ax.scatter(np.arange(0,simlen,1),y1_1,y1_2,"ro")
# plt.plot(y0_1,y0_2,"go")
# plt.plot(y1_1,y1_2,"ro")

plt.show()