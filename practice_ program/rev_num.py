num=int(input("please enter a number:-"))
revnum=0
if num<=0:
    print("please enter the valid number")
else:
    while num>0:
        digit=num%10
        revnum=revnum*10+digit
        num=num//10
    print("the reverse num is:-",revnum)
        