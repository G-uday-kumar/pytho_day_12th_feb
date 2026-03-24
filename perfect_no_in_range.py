
def checkperfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    return sum

if __name__ == '__main__':
    # num=int(input("enter the number :-"))
    for k in range(1,10000):
        num=k

        sum=checkperfect(num)
        if sum==num:
            print(num)


