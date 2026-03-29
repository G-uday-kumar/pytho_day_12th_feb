def count_digits(num):
    count=0
    while num!=0:
        count+=1
        num=num//10
    return count
def check_arm(num):
    count = count_digits(num)
    res = 0
    while num!=0:
        rem=num%10
        res=res+rem**count
        num//=10
    return res


if __name__=="__main__":
    k=1
    for k in range(1,1000):
        num=k
        res=check_arm(num)
        if num==res:
            print("This number is armstrong:-",num)


