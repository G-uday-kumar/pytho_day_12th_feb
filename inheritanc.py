class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print("Hi",self.ename)
        print("your sal is:-",self.esal)


class Test:
    def modify(emp):
        emp.esal+=12000
        emp.display()#calling the display method of a Employee class with emo reference
    # def display(emp):
    #     print(emp.esal)

e=Employee(101,"uday",40000)
Test.modify(e)
# Test.display(e)
# Test.display(e)


