from scipy.fftpack import fft2, ifft2
from matplotlib import pyplot as plt
import imageio as ima
import numpy as np
from matplotlib.colors import LogNorm

#записываю изображение в массив и убираю измерение с цветами
image = ima.imread('nature.jpg')
image = image[:,:, 0]


#преобразования фурье: прямое и обратное
fourier_img = fft2(image)
fabs = np.abs(fourier_img)
plt.imshow(fabs, cmap='gray', norm=LogNorm())
plt.show()
original_img = ifft2(fourier_img) 



#вычисляю минимум и середину между средним и максимальным значениями
max_val = np.max(fabs)
mean_val = np.mean(fabs)
min_val = np.min(fabs)
k = (max_val + mean_val)/2

x = []
y = []
fourier = fft2(image)


#делю промежуток от минимума до почти максимума значений на 100 равных промежутков
for i in range(100, 0, -1):
    #вычисляю границу значений, ниже которой я зануляю элементы
    step = min_val + (k - min_val)/i
    low_elem = fabs < step
    fourier[low_elem] = 0
    zero = sum(np.count_nonzero(fourier, 0))
    #вычисляю долю ненулевых элементов
    coef = zero/image.size
    x.append(coef)
    reconstr = ifft2(fourier)
    #вычисляюкачество изображения при определенной доле коэффициэнтов  
    quality = np.linalg.norm(original_img - reconstr)/np.linalg.norm(original_img)
    y.append(quality)
    
plt.plot(x,y)
plt.xlabel("Доля коэффициэнтов")
plt.ylabel("Качество изображения")
plt.show()
    

