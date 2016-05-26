import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

data=np.loadtxt(raw_input('file name:'))
data_t=np.transpose(data)

logTe=data_t[5]
logg=data_t[6]

plt.plot(logTe,logg,'b.')
plt.xlabel('logTe')
plt.ylabel('logg')
plt.ylim(plt.ylim()[::-1])
plt.xlim(plt.xlim()[::-1])
plt.show()

