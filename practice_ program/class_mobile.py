#Python program for the class Mobile
class Mobile:
    def switch_off(self):
        print("mobile is Switching off")
    def switch_on(self):
        print("mobile is Switching on")
    def listen_music(self):
        print("mobile is listening music")
m=Mobile()
m.brand="Oppo"
m.price=10000
m.color="blue"
print(m.brand)
print(m.price)
print(m.color)

class Person:
    def starts_phone(self):
        self.m=Mobile()
        print("mobile is starting phone")
        self.m.switch_off()
        self.m.switch_on()
        self.m.listen_music()
p=Person()
p.starts_phone()

