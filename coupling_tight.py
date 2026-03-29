from abc import ABC,abstractmethod

class Developer(ABC):
    @abstractmethod
    def developer(self):
        pass
class Frontendcoding(Developer):
    def developer(self):
        print("Frontendcoding developer works on")
class Backendcoding(Developer):
    def developer(self):
        print("Backendcoding developer works on")

class Company:
    def __init__(self,d):
        self.dev = d
    def work(self):
        self.dev.developer(self)
        print("Company developer works on")
d=Backendcoding
c=Company(d)
c.work()

d=Frontendcoding
c=Company(d)
c.work()

