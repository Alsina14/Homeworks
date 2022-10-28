from math import sin

class FunctionCaller:
    def __init__(self, func):
        self.func = func
        self.list = []
        
    def append_job(self, x):
        self.x = x
        self.list.append(x)
             
    def call(self):
        if self.list:
            for i in range(len(self.list)):
                print(f"Calling for job {self.list[i]}. Result:", self.func(self.list[i]))
            del self.list[0:]
        else:
            print("Nothing to do")
            
        
        
        
        
test = FunctionCaller(sin)
test.append_job(0)
test.append_job(1)
test.append_job(3.1415)
test.call()
test.call()