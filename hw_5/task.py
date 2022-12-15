import numpy as np
from matplotlib import pyplot as plt
from task_9 import depth_list
from time import perf_counter
from scipy.optimize import curve_fit



def list_mul_time(l1: list, l2: list):
        
    if depth_list(l1) == 1:
        t1 = perf_counter()
        l = [x*y for x, y in zip(l1,l2)]
        t2 = perf_counter()
        t = t2 - t1
            
    elif depth_list(l1) == 2:
        t1 = perf_counter()
        l = [[x*y for x, y in zip(x1,y1)] for x1, y1 in zip(l1,l2)]
        t2 = perf_counter()
        t = t2 - t1
            
    elif depth_list(l1) == 3:
        t1 = perf_counter()
        l = [[[x*y for x,y in zip(f,e)] for f,e in zip(i,j)] for i,j in zip(l1,l2)]
        t2 = perf_counter()
        t = t2 - t1
        
    return t


def array_mul_time(ar1, ar2):
    t1 = perf_counter()
    ar = ar1*ar2
    t2 = perf_counter()
    t = t2 - t1
    return t
    

dimlist = [1, 10, 20, 30, 40, 50]
arr1 = np.empty((100, len(dimlist)))
arr2 = np.empty((100, len(dimlist)))
arr3 = np.empty((100, len(dimlist)))
t1 = np.empty((100, len(dimlist)))
t2 = np.empty((100, len(dimlist)))
t3 = np.empty((100, len(dimlist)))




for k in range(100):
    for j, i in enumerate(dimlist):
    
        myArray1 = np.random.random((i))
        myArray2 = np.random.random((i ,i))
        myArray3 = np.random.random((i, i, i))
    
        arr1[k][j] = array_mul_time(myArray1, myArray1)
        arr2[k][j] = array_mul_time(myArray2, myArray2)
        arr3[k][j] = array_mul_time(myArray3, myArray3)
    
        mylist1 = myArray1.tolist()
        mylist2 = myArray2.tolist()
        mylist3 = myArray3.tolist()
    
        t1[k][j] = list_mul_time(mylist1, mylist1)
        t2[k][j] = list_mul_time(mylist2, mylist2)
        t3[k][j] = list_mul_time(mylist3, mylist3)
        
time1 = np.mean(t1, axis = 0)  
time2 = np.mean(t2, axis = 0)   
time3 = np.mean(t3, axis = 0)
atime1 = np.mean(arr1, axis = 0)
atime2 = np.mean(arr2, axis = 0)
atime3 = np.mean(arr3, axis = 0)
err1 =  np.std(t1, axis = 0)
err2 =  np.std(t2, axis = 0)
err3 =  np.std(t3, axis = 0)
aerr1 =  np.std(arr1, axis = 0)
aerr2 =  np.std(arr2, axis = 0)
aerr3 =  np.std(arr3, axis = 0) 


def polinom1(x, a, b):
    return a*x + b
    
def polinom2(x, a, b, c):
    return a*x**2 + b*x + c

def polinom3(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d

x = np.arange(51)

args, _ = curve_fit(polinom1, dimlist, np.log(atime1))    
a, b = args[0], args[1]
y1 = polinom1(x, a, b) 

args, _ = curve_fit(polinom1, dimlist, np.log(atime2))    
a, b = args[0], args[1]
y2 = polinom1(x, a, b) 

args, _ = curve_fit(polinom1, dimlist, np.log(atime3))    
a, b = args[0], args[1]
y3 = polinom1(x, a, b) 

args, _ = curve_fit(polinom3, dimlist, np.log(time1))    
a, b, c, d = args[0], args[1], args[2], args[3]
y_fit1 = polinom3(x, a, b, c, d)

args, _ = curve_fit(polinom3, dimlist, np.log(time2))    
a, b, c, d = args[0], args[1], args[2], args[3]
y_fit2 = polinom3(x, a, b, c, d)

args, _ = curve_fit(polinom3, dimlist, np.log(time3))    
a, b, c, d = args[0], args[1], args[2], args[3]
y_fit3 = polinom3(x, a, b, c, d)



fig, ax = plt.subplots(2, figsize = (10, 8))

ax[0].set_title("Dependence of the multiplication time of lists and arrays on their length")
ax[0].set_xlabel("Size of lists")
ax[0].set_ylabel("log(Time)")
ax[0].plot()
ax[0].plot(x, y_fit1, c = 'r', label = "1-dim list approximation")
ax[0].plot(x, y_fit2, c ='g', label = "2-dim list approximation")
ax[0].plot(x, y_fit3, c = 'b', label = "3-dim list approximation")
ax[0].errorbar(dimlist, np.log(time1), yerr = np.log(err1), fmt = 'ro')
ax[0].errorbar(dimlist, np.log(time2), yerr = np.log(err2), fmt = 'g^')
ax[0].errorbar(dimlist, np.log(time3), yerr = np.log(err3), fmt = 'bs')
ax[0].legend()

ax[1].set_xlabel("Size of arrays")
ax[1].set_ylabel("log(Time)")
ax[1].plot(x, y1, 'r', label = "1-dim array approximation")
ax[1].plot(x, y2, 'g', label = "2-dim array approximation")
ax[1].plot(x, y3, 'b', label = "3-dim array approximation")
ax[1].errorbar(dimlist, np.log(atime1), yerr = np.log(aerr1), fmt = 'ro')
ax[1].errorbar(dimlist, np.log(atime2), yerr = np.log(aerr2), fmt = 'g^')
ax[1].errorbar(dimlist, np.log(atime3), yerr = np.log(aerr3), fmt = 'bs')
ax[1].legend()

fig.tight_layout()
     


