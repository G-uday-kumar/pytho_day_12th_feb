class OS:
    def __init__(self):
        print("os is working")
    def checkOs(self):
        print("os is installed  and its working")
class Charger:
    def __init__(self):
        print("charger is created")

    def getCharger(self):
        print("charger is still working")


class Mobile:
    def __init__(self):
        self.o=OS()
        print("now staretd running of mobile objetc")
    def hasA(self,charger):
        print("charger is staretd running of mobile object")

m=Mobile()
m.o.checkOs()
c=Charger()
c.getCharger()
m.hasA(c)
# m=None#mobile object destroying here
c.getCharger()
# m.hasA()

