def reversed(num):
    res=0
    while num!=0:
        rem=num%10
        num=num//10
        res=(res*10)+rem
    return res


if __name__=='__main__':
    count=0
    for k in range(1,10000):
        num=k

        rev=reversed(num)
        if num==rev:
            print(num)
            count=count+1
        if count==50:
            break
