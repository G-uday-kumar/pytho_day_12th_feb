class Car:
    def start(self):
        print("Car is starting")
    def shiftgear(self,gn):
        print("Shifting gear to",gn,"gear")
        if gn==0:
            self.stop()
    def stop(self):
        print("Car is stopped")
class Driver:
    def driver(self):
        self.c=Car()
        print("Driver is starting")
        self.c.start()
        self.c.shiftgear(1)
        self.c.shiftgear(3)
        self.c.shiftgear(5)
        print("Driver is stopped due to high speed driving")
        self.c.shiftgear(0)
        print("Driver is stopped due to speed driving")
d=Driver()
d.driver()