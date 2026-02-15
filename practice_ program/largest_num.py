num=int(input("enter the number:- "))
largest=0
while num>0:
    dig=num%10
    if dig>largest:
        largest=dig
        
    num=num//10
print("the largets num is:-",largest)