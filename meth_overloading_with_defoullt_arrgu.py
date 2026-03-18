class Artel:
    def reacharge(self,car_num=None,cvv=None,exp_date=None,user_name=None,password=None,upi_id=None,pin=None):

        if car_num and cvv and exp_date:
            print("reacharge done by card")
            print("card num is",car_num)
        elif user_name and password:
            print("reacharge done by user with the net banking")
            print("user name is",user_name)

        elif upi_id and pin:
            print("reacharge done by user with the UPI")
            print("upi id is",upi_id)
        else:
            print("reacharge not done by user or upi or card so give vaid input")
a=Artel()
print(a.reacharge( car_num="123456765432",cvv="233",exp_date="2/34"))
print(a.reacharge(user_name="uhudas",password="233"))