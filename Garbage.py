import sys
import time
class Demo:
    def __init__(self):
        print("COnstructor get executed")
    def __del__(self):
        print("Destructor get executed")
d1=Demo()
d2=d1
d3=d2

del d1
print("Object not destroyed after removing d1:--")
time.sleep(5)

del d2
print("Object not destroyed after removing d2:--")
time.sleep(5)
del d3
print("trying to remove d3")
time.sleep(5)

time.sleep(5)
print("ENd of")
print(sys.getrefcount(d1))
print(sys.getrefcount(d2))
print(sys.getrefcount(d3))