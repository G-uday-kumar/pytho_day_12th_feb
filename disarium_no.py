def check_disarium(num):
    digit=count_digit(num)
    res=0
    while num!=0:
        rem=num%10
        num=num//10
        res=res+rem**digit
        digit-=1
    return res


def count_digit(num):
    count=0
    while num!=0:
        num=num//10
        count+=1
    return count


if __name__=="__main__":
    num=135
    res=check_disarium(num)
    if res==num:
        print("The number is disarium")
    else:
        print("The number is not disarium")