class Vehicle:
    def __init__(self,vehicle_no,brand,fuel_type):
        self.vehicle_no = vehicle_no
        self.brand = brand
        self.fuel_type = fuel_type

    def start(self):
        print("vehicle get started")
    def stop(self):
        print("vehicle stopped")
    def display(self):
        print("vehicle display details are", self.vehicle_no, self.brand, self.fuel_type)

class Bike(Vehicle):
    def kickstart(self):
        print("bike kick start")

class Car(Vehicle):
    def openTrunk(self):
        print("car open trunk")
class ElectricVehicle(Vehicle):

    def chargbattery(self, battery_level):
        self.battery = battery_level
        print("electric battery charging")
    def checkbatterlevel(self):
        print("electric battery level", self.battery)

b=Bike("KA 35 EN 5818","Honda","Petrol")
b.start()
b.stop()
b.display()
b.kickstart()

c=Car("KA 35 EN 1818","Honda","Deicel")
c.start()
c.stop()
c.display()
c.openTrunk()


e=ElectricVehicle("KA 35 EN 1818","Honda","Power Supply")
e.start()
e.stop()
e.display()
e.chargbattery("78%")
e.checkbatterlevel()