import numpy as np
from scipy.fftpack import fft2, ifft2, fftshift
from astropy.io import fits
from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm

data = fits.getdata("noised.fits")
plt.imshow(data, cmap='gray', norm=LogNorm())
plt.show()

fdata = fft2(data)
plt.imshow(np.abs(fdata),cmap='gray', norm = LogNorm())

shifted = fftshift(fdata)
plt.imshow(np.abs(shifted),cmap='gray', norm = LogNorm())
plt.show()

#Приближыю
new_fdata = shifted[790:850, 850:950]
plt.imshow(np.abs(new_fdata),cmap='gray', norm = LogNorm())
plt.show()

#Зануляю координаты пикселей,которые создают шум
noiseless = shifted
noiseless[804,881] = 0
noiseless[834,911] = 0

plt.imshow(np.abs(noiseless[790:850, 850:950]),cmap='gray', norm = LogNorm())
plt.show()


new_data = ifft2(noiseless)
plt.imshow(np.abs(new_data),cmap='gray', norm = LogNorm())
plt.show()