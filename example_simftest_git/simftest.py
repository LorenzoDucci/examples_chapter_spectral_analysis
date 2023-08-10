import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import matplotlib.colors as colors
from scipy import stats

data = np.loadtxt("simftest_output.dat")

dd=data[:,2]

plt.figure()
plt.hist(dd,bins=500)
plt.xlabel('Change in W statistic')
plt.ylabel('Number')
plt.yscale('log')
#plt.xscale('log')
plt.axis([-20, 50,0.7,1000])
xcoords = [13.561833400000069]
for xc in xcoords:
    plt.axvline(x=xc ,color='red', linestyle='--')
plt.tight_layout() 
plt.savefig('simftest_plot.eps')

j=0
for i in range(len(dd)):
    if (dd[i] >= xcoords):
        j=j+1

print('Probability that data are consistent with model without extra component = ',float(j)/float(len(dd)))
