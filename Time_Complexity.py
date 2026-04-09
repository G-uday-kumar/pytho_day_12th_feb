import math

if __name__ == '__main__':
    n=int(input("cdcd:-"))
    for i in range(1,n+1):
        if n%i==0:
            print(i)

    n = int(input("cdcd:-"))
    for i in range(1, (n//2) + 1):
        if n % i == 0:
            print(i)
    print(n)

    n = int(input("cdcd:-"))
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(i)
            print(n/i)

    n = int(input("cdcd:-"))
    for i in range(1,int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(i)
    for i in range(int(math.sqrt(n)) + 1, 0, -1):
        if n % i == 0 and n/i!=i:
            print(n//i)
            # print(n / i)