from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self):
        self.area=None
    @abstractmethod
    def input(self):
        pass
    @abstractmethod
    def calArea(self):
        pass
    @abstractmethod
    def disp(self):
        pass

class Rectangle(Shape):
    def input(self):
        self.l=int(input("enter l"))
        self.h=int(input("enter h"))
    def calArea(self):
        self.area=(self.l*self.h)
    def disp(self):
        print("the area is:-",self.area)

class Square(Shape):
    def input(self):
        self.l=int(input("enter l"))
    def calArea(self):
        self.area=(self.l*self.l)
    def disp(self):
        print("the area is:-",self.area)

class Circle(Shape):
    def input(self):
        self.r=int(input("enter r"))
    def calArea(self):
        self.area=(self.r*self.r*3.14)
    def disp(self):
        print("the area is:-",self.area)