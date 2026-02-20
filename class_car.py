class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(self.brand, "car has started")

    def stop(self):
        print(self.brand, "car has stopped")
car1 = Car("Toyota", "Red")
car1.start()
car1.stop()