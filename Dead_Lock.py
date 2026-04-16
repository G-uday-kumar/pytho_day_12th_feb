import  time
from threading import Thread, Lock, current_thread


class DBThread:
    def __init__(self):
       self.r1=Lock()
       self.r2=Lock()
       self.r3=Lock()

    def run(self):
        if current_thread()=="Rama":
            self.aquire_Rama()
        else:
            self.aquire_Sitha()
        # pass
    def aquire_Rama(self):
        with self.r1:
            print("Rama Aquires oracle")
            time.sleep(1)

            with self.r2:
                print("Rama Aquires Sybase")
                time.sleep(1)


                with self.r3:
                    print("Rama Aquires informa")
                    time.sleep(1)

    def aquire_Sitha(self):
        with self.r2:
            print("Sitha Aquires Sybase")
            time.sleep(1)
            with self.r3:
                print("Sitha Aquires informa")
                time.sleep(1)
                with self.r1:
                    print("Sitha Aquires oracle")
                    time.sleep(1)

db=DBThread()
t1=Thread(target=db.aquire_Rama, name="Rama")
t2=Thread(target=db.aquire_Sitha, name="Sitha")


t1.start()
time.sleep(1)
t2.start()

# db.aquire_Rama()
# db.aquire_Sitha()