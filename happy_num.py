def sum_of_sq_digits(num):
    res=0
    while num!=0:
        rem=num%10
        num//=10
        res=res+rem*rem
    return res

if __name__=="__main__":
    num=int(input("enter a number to check the number is happy or not:-"))
    res=sum_of_sq_digits(num)
    # print(res)
    while res!=0 and res!=4:
        res=sum_of_sq_digits(res)
        print(res)

    if num==1:
        print("happy number")
    else:
        print("not happy number")