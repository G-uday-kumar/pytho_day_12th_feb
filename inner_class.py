class Person:
    def __init__(self):
        self.name="uday"
        self.db=self.Dob()
        print("the name is :- ",self.name)
    class Dob:
        def __init__(self):
            self.dd=28
            self.mm=6
            self.yy=2004
        def display(self):
            print("Dob is:-",self.dd,"-",self.mm,"-",self.yy)
p=Person()
p.db.display()