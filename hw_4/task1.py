from multiprocessing import Pool
from time import perf_counter


def fibo(n):
    '''Выяисляет n-ое число Фибоначчи'''
    fib1 = 1
    fib2 = 1
 
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return fib2



time_list = []

if __name__ == '__main__':
    for i in range(1, 17):
        #фиксируем время до распараллеливания
        t0 = perf_counter()
        for _ in range(20):
            #даем вычислять функцию разному количеству процессов
            with Pool(i) as p:
                res = sum(p.map(fibo, list(range(3,50))))
        #фиксируем время после параллельных вычислений
        t1 = perf_counter()
        t = t1 - t0
        time_list.append(t)
#получаем индекс минимального элемента (времени вычислений) списка, начиная с 1, то есть количество ядер  
num = min(range(len(time_list)), key = lambda i: time_list[i]) + 1
print(f"Количество ядер: {num}")     