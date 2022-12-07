from queue import Queue
import threading
import random 

#объект очереди
qu = Queue()

class Sender:
    '''при инициализации добавляет в очередь слово, при вызове добавляет в
    очередь num чисел от 0 до 1 и слово'''
    def __init__(self, num):
        self.number = num
        qu.put("beginning")
        
    def __call__ (self):
        for _ in range(self.number):
            qu.put(random.random())
        qu.put("ending")


class Reciever:
    '''проводит вычисления с данными из очереди, пока количество первых слов не
    сравняется с количеством последних слов (то есть все данные будут обработаны)'''
    def  __init__(self):
        self.counter = 0

    def __call__(self):
        k = 1
        while True:
            element = qu.get()
            if element == "beginning":
                self.counter += 1
            elif element == "ending":
                self.counter -= 1
            else:
                s = 2*element
                print(f"{k}: 2 * (gotten element) = {s}")
                k += 1

            if (self.counter == 0):
                break
            

sender_list = []
for i in range(10):
    sender_list.append(Sender(i+1))

#вызываю 10 потоков Sender и 1 Reciever

for sender in sender_list:
    threading.Thread(target = sender).start()


threading.Thread(target = Reciever()).start()