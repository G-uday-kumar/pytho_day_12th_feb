i = 1
while i <= 5:
    print(i)
    i += 1

print(" \nGuesssing the correct number from the in the range of 1-100")
secret=18
i=int(input("enter the number to guess my fav cricketor:-"))
while i!=secret:
    print("your guess is wrong the number try again!!!!")
    i=int(input("enter the number to guess my fav cricketor:- "))
print("your guess is correct the numbe is 18 its VK")

print("\nPrinting the tables of the 18")
n=18
table=0
i=1
while i<11:
    table=i*n
    print(n,"X",i,"=",table)
    i+=1