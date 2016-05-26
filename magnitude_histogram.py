import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt('output.txt')
data_t=np.transpose(data)

x_axis=data_t[11]

plt.hist(x_axis,bins=1000)
#plt.title('Kepler Magnitudes for objects around KOI 3158')
plt.xlim(0,np.max(data_t))
plt.xlabel('Magnitude')
plt.ylabel('Number of objects')
plt.show()


