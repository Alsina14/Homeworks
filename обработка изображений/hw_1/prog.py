from matplotlib import pyplot as plt
import numpy as np
from itertools import product
from astropy.io import fits

data = np.empty((100, 200, 200))
for i in range(100):
    data[i,] = fits.getdata("data.fits", i+1)

    

image_mean = np.mean(data, 0)
image_median = np.median(data, 0)



def circle(r, image, c):
    s = 0
    for i,j in product(range(200), repeat = 2):
        if (i - c[0])**2 + (j - c[1])**2 <= r**2:
            s += image[i,j]
    return s
 
c = [100, 100]   
radius = range(40)
flow1 = np.empty(len(radius))
flow2 = np.empty(len(radius))
for r in radius:
    flow1[r] = circle(r, image_mean, c)
    flow2[r] = circle(r, image_median, c)
    
    
fig, ax = plt.subplots(2, 2)  
ax[0][0].imshow(image_mean)
ax[0][0].title.set_text('mean')
ax[0][1].imshow(image_median)
ax[0][1].title.set_text('median')
ax[1][0].plot(range(200), (image_mean[100,] + image_mean[101,])/2)
ax[1][0].plot(range(200), (image_median[100,] + image_median[101,])/2)
ax[1][0].legend(['mean','median'])
ax[1][1].plot(radius, flow1)
ax[1][1].plot(radius, flow2)
ax[1][1].legend(['mean','median'])
plt.show()

    