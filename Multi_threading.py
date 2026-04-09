from threading import Thread
import time
class Task1(Thread):
    def run(self):
        for i in range(2):
            print("welcome to my bank")
            print("Hello Uday")
            time.sleep(2)#seconds

class Task2(Thread):
    def run(self):
        for i in range(5):
            print("Hello Uday")
            time.sleep(5)
class Task3(Thread):
    def run(self):
        a=1000
        b=2000
        print(a+b)
t1=Task1()
t2=Task2()
t3=Task3()
t1.start()
t2.start()
t3.start()