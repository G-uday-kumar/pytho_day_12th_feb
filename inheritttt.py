class Person:
    def __init__(self, name):
        self.name = name


class Uday(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def display(self):
        print(self.name, self.salary)


u = Uday("Uday", 20000)
u.display()