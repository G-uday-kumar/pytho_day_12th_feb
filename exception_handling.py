try:
    num=int(input("enter a number"))
    div=100/num
    print(div)
except :
    print("div not possible")


try:
    num=int(input("enter a number"))
    div=100/num
except ValueError:
    print("div not possible bczz values are invalid")
except ZeroDivisionError:
    print("div not possible zero cant be divisble")
try:
    num=int(input("enter a number"))
    div=100/num
    print(div)
except ZeroDivisionError:
    print("div not possible with zero")
except ValueError:
    print("div not possible with invalid value")
else:
    print("div is equal :- ",div)
finally:
    print("try again or execution completed")

try:
    num=int(input("enter a number"))
    div=50/num
except ZeroDivisionError:
    print("div not possible with Zero ")
except ValueError:
    print("div not possible")
else:
    print("div is equal :- ",div)
finally:
    print("try again or execution completed")