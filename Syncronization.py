import time
from threading import Thread, current_thread
import threading
class House:
    def __init__(self):
        self.lock = threading.Lock()
        t1=Thread(target=self.run,name="Boy")
        t2 = Thread(target=self.run, name="Girl")
        t3=Thread(target=self.run,name="Other")

        t1.start()
        time.sleep(1)
        t2.start()
        time.sleep(1)
        t3.start()

    def run(self):
        with self.lock:
            print(current_thread().name," Entered the Bathroom")
            time.sleep(2)
            print(current_thread().name," closed the Door Bathroom")
            time.sleep(2)
            print(current_thread().name," is taking bath")
            time.sleep(2)
            print(current_thread().name," is dressing Up")
h=House()
