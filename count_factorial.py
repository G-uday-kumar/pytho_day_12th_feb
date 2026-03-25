def factorial(n):
    count = 0
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        count=count+1
    print(count)
    return fact
    # if n==0:
    #     return 0
    # elif n==1:
    #     return 1
    # else:
    #     count=count+1
    #     return n*factorial(n-1)
if __name__=="__main__":

    num=int(input("enter the number"))
    fact=factorial(num)
    print(fact)
    # print(count)
