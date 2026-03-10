class Mobile:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year

class smartphone(Mobile):
    def __init__(self,price,brand,year):
        self.price=price
        super().__init__(brand,year)#used to call the parent class constructor

    def display(self):
        print(self.brand,self.price,self.year)
s=smartphone(20000,"iphone",2020)
s.display()
s1=smartphone(12200,"one",2024)
s1.display()


class Animal:
    def __init__(self,name):
        print()
        print("animal",name)

class Dog(Animal):
    pass
c=Dog("sayed")

