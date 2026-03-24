
def checkperfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    return sum

if __name__ == '__main__':
    num=int(input("enter the number :-"))
    sum=checkperfect(num)
    if sum==num:
        print("perfect number")
    else:
        print("not perfect number")


