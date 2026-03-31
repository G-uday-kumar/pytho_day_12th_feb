def sum_of_digit(num):
    res=0
    while num!=0:
        rem=num%10
        num//=10
        res=res+rem
    return res


if __name__=="__main__":
    num=14
    new_num=num+1
    while sum_of_digit(num)*2 !=sum_of_digit(new_num):
        new_num+=1
    print(new_num)
