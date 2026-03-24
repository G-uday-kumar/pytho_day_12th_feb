def reversed(num):
    res=0
    while num!=0:
        rem=num%10
        res=res*10+rem
        num=num//10
    return res

if __name__ == '__main__':
    for k in range(1,10000):
        num=k
        rev=reversed(num)
        if rev==num:
            print(num)