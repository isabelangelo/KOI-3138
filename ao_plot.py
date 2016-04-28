import numpy as np
import matplotlib.pyplot as plt

aosep=np.loadtxt('aosep.txt')
aodjmag=np.loadtxt('aodjmag.txt')

Jp=13.379
Kp=17.131

J=Jp+aodjmag
K=J+0.1918+J*0.08156

aodkmag=K-Kp
aosep[0]=aosep[2]
aosep[1]=aosep[2]

plt.plot(aosep,aodjmag,'b--',label='J mag')
plt.plot(aosep,aodkmag,'g',label='Kep mag')
plt.ylim(plt.ylim(0,12)[::-1])
plt.xlim(0,3)
plt.show()
