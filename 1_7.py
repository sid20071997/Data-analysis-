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

print (coin(4))