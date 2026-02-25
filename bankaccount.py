class BankAccount:
    def __init__(self,name,amount):
        self.amount=amount
        self.name=name
    def deopsit(self,name,amount):

        if name==self.name:
            print("the credentials are correct now you can add the amount to the rgt person")
            amount=int(input("enetre the value of amount you want to add :"))
            self.amount=self.amount+amount
            print("total amount is :",self.amount)
        # else:
            print("invalid credetials")



    def withdraw(self,amount):
        amount=int(input("enetr amount to withdrawa: "))
        if amount < self.amount:
            self.amount=self.amount-amount
            print("amount withdrawed successfully:",amount)
        else:
            print("insufficient money")

        # self.amount=amount
    def display(self):
        print("the remaining amount is : ", self.amount)

class person:
    def start_trans(self):
        self.b=BankAccount()
        self.b.amount=1000
        print("now you cn start")
        self.b.deopsit("uday",1000)
        self.b.withdraw(100)
        self.b.display()
#
# b=BankAccount()
# b.name="Udya"
# b.balance=10000
# print(b.balance)
p=person()
p.start_trans()