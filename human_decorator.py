class Human:
    def __init__(self):
        self.__age=None
        # self.__name="uday kumar"

    @property
    def age(self):
        # print("your name is",name)
        return self.__age
    @age.setter
    def age(self,A):
        if (A>120 or A<0):
            print("the age must be between 0 and 120")
        elif (A>18):
            self.__age=A
        else:
            print("you are still younger")
h=Human()
h.name="uday kumar"
h.age=int(input("enter your age:-"))
print("Hi..",h.name)
print("your age is",h.age)
