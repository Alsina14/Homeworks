from pathlib import Path
from datetime import datetime
import time

mypath = Path(input("Input the path to directory:"))

n = 120

while n > 0:
    paths = list(mypath.glob('*'))
    A = set(map(lambda x: x.name, paths))
    time.sleep(1)
    paths = list(mypath.glob('*'))
    B = set(map(lambda x: x.name, paths))
    
    if len(B) > len(A):
        C = B - A
        print(datetime.now().time(), 'file', C,  "was created")
    elif len(B) < len(A):
        C = A - B
        print(datetime.now().time(), 'file', C,  "was removed")
    
    n = n-1