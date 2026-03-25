def reversed(num):
    res=0
    while num!=0:
        rem=num%10
        num=num//10
        res=res*10+rem
    return res
if __name__=='__main__':
    k=1
    count=0
    while(True):
        num=k
        res=reversed(num)
        if num==res:
            print(num)
            count=count+1
        if count==50:
            break
        k+=1 