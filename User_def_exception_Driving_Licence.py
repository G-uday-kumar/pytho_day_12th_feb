class UnderAgeException(Exception):
     pass
class OverAgeException(Exception):
    pass
class Driving_Licence:
    def __init__(self,age):
        self.age = age
    def Check_age(self  ):
        try:
            if self.age < 18:
                raise UnderAgeException()
            elif self.age > 60:
                raise OverAgeException()
            else:
                print("You are belongs  under age category you can reciev DL")
        except UnderAgeException:
            print("You are under age category you wait upto age 18 to reciev DL")
        except OverAgeException:
            print("you are alreay a retaired age so you not eligibel for DL application")
        except Exception:
            print("you got unknow error")
        finally:
            print("you have to checked your age")
d=Driving_Licence(17)
d.Check_age()