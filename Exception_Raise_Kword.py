class Demo:
    def login(self):
        print("1.enetr to the login page")
        try:
            self.account()
        except Exception:
            print("2.login failed due to some error")
    def account(self):
        print("anow logint to the ccount page")
        try:

            un="uday"
            pas="password"
            print("the user name is ",user_name)
        except Exception:
            print("the user name is wrong in the account")
            raise

print("now staerts the main logic")
d=Demo()
try:
    d.login()
except Exception:
    print("login failed due to some error")
print("exitig  normally")
