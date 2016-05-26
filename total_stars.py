import numpy as np

#convert and reshape arrays of stars and radii:
stars=np.array([210675,152329,114545,109607,108826,108000,108826,110028,110028,105843,106669,107124,106275,107124,106275,107576,109231,108000,108382,109231,109231,107124])
radii=np.array([.97,1.78,2.62,3.46,4.33,5.18,6.04,6.89,7.76,8.61,9.46,10.33,11.19,12.05,12.91,13.77,14.63,15.49,16.35,17.21,18.06,18.92])

#converting to star density in stars per square arcsecond:
star_densities=stars/12960000.

#creat an array of total stars in each annulus:
total_stars=[]
for i in range(21):
    if i==0:
        b=star_densities[i]*3.1416*radii[i]**2
        total_stars.append(b)
    else:
        c=star_densities[i]*(3.1416*radii[i]**2-3.1416*radii[i-1])
        total_stars.append(c)

print sum(total_stars)
    


    
