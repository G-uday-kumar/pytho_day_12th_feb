class Card:
    def __init__(self, card_no, cvv, exp_date):
        self.card_no = card_no
        self.cvv = cvv
        self.exp_date = exp_date

    def withdraw(self):
        print("amount withdrawd successfully")

    def swipe(self):
        print("card swiped successfully")

    def check_balance(self):
        print(" balance checked successfully")


class Debitcard(Card):
    def deposit(self, amount):
        print("amount deposited successfully")

class CreditCard(Card):
    creditLimit=100000
    def paybill(self):
        print("amount paybill successfully")
class Forex(Card):
    rootCurrency="INR"
    targetCurrency="EUR"
    def loadamount(self,amount):
        print("amount loaded successfully")
    def convert(self):
        print("amount converted successfully from",self.rootCurrency,"to",self.targetCurrency)


d=Debitcard(card_no="123352",cvv="123",exp_date="2/40")
print(d.card_no,d.cvv,d.exp_date)
d.withdraw()
d.deposit(10000)
d.swipe()
d.check_balance()

print(",,,,,,,,,,,,,,,,,,,,,,,,,,")
f=Forex(card_no="1233",cvv="1223",exp_date="2/60")
print(f.card_no,f.cvv,f.exp_date)
f.withdraw()
f.swipe()
f.loadamount(12322)
f.convert()
f.check_balance()
print(",,,,,,,,,,,,,,,,,,,,,,,,,,")
c=CreditCard(card_no="1233",cvv="123",exp_date="2/60")
print(c.card_no,c.cvv,c.exp_date)
c.withdraw()
c.swipe()
c.paybill()
c.check_balance()
