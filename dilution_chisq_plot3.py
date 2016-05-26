import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt('dilution_chisq.txt')

dilution=data[0]
chisq=data[3]
scaled_chisq=chisq*158

plt.plot(dilution,scaled_chisq,'ro')
plt.xlim(0,1)
plt.xlabel('dilution')
plt.ylabel('chi-squared')
plt.show()


