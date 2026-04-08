import time
class Demo:
    def Banking(self):
        self.username=input("enter your username")
        self.password=input("enter your password")
        print("collect your cash")
    def print(self):
        for i in range(5):
            print("Hi Uday Kumar")
            time.sleep(5)
    def add(self):
        a=10
        b=20
        print(a+b)
d=Demo()
d.Banking()
d.print()
d.add()
d.Banking()
d.print()