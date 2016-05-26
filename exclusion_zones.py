import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#loading and defining variable arrays
UKIRT_data=np.loadtxt('UKIRT.txt')
UKIRT=np.transpose(UKIRT_data)
ukirt_separation=UKIRT[4][1:]
ukirt_dmag=UKIRT[8][1:]

speckle_separation=np.arange(0.1,1.3,0.1)
speckle_dmag=np.array([4.64,5.64,6.1,6.1,6.1,6.15,6.2,6.25,6.25,6.25,6.25,6.25])

ao_separation=np.loadtxt('AOsep.txt')
ao_djmag=np.loadtxt('AOdjmag.txt')
Jp=13.379
Kp=17.131
J=Jp+ao_djmag
K=J+0.1918+J*0.08156
ao_dkmag=K-Kp
#setting zero point:
ao_separation[0]=ao_separation[2]
ao_separation[1]=ao_separation[2]

#plotting the lines and setting graph size
fig,ax=plt.subplots()
plt.plot(ukirt_separation,ukirt_dmag,linestyle='-')
plt.plot(speckle_separation,speckle_dmag,linestyle='-',color='g')
plt.plot(ao_separation,ao_dkmag,linestyle='-',color='indigo')
plt.ylim(plt.ylim(0,6.5)[::-1])
plt.xlim(0,3)
plt.axhline(y=5.792,color='r')

#labeling graph
plt.xlabel('Separation (arcsec)',family='serif')
plt.ylabel('Magnitude Difference',family='serif')
plt.title('Exclusion Zones for KOI-3138',family='serif')

#filling in exclusion zones
ax.axhspan(5.792,7,alpha=0.5,facecolor='r',hatch='XXX',edgecolor='r')
ax.fill_between(ao_separation,ao_dkmag,0,facecolor='mediumpurple',hatch='XXX',edgecolor='indigo',alpha=0.5)
ax.fill_between(speckle_separation,speckle_dmag,0,facecolor='aquamarine',hatch='XXX',edgecolor='g',alpha=0.5)
ax.fill_between(ukirt_separation,ukirt_dmag,0,facecolor='LightBlue',hatch='XXX',edgecolor='b',alpha=0.5)
plt.show()

