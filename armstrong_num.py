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
    num=int(input("Enter a number: "))


    res=check_arm(num)
    if num==res:
        print("The number is armstrong:-",num)
    else:
        print("The number is not armstrong:-",num)

