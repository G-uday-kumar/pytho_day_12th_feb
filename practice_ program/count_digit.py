
number=int(input("enter the number"))
if number<=0:
    print("please enter the valid number")
else:
    count=0
    while number>0:
        number=number//10
        count=count+1
    print("total numbers of digits are :-",count)