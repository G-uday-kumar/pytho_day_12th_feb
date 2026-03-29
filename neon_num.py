def check_neon(num):
    res=0
    while num!=0:
        rem=num%10
        num//=10
        res=res+rem
    return res

if __name__=="__main__":
    for k in range(1,1000000):
        num=k
        sq = num*num
        res=check_neon(sq)
        if res==num:
            print(num)
