if __name__ == '__main__':
    # arr = [4, 5, 3, 2, 9]
    # maxi=0
    # l=3
    # for i in range(0,l):
    #     maxi+=arr[i]
    # for i in range(0, len(arr)):
    #     for j in range(i, len(arr)):
    #         sum=0
    #         count=0
    #         for k in range(i, j + 1):
    #             sum+=arr[k]
    #             count+=1
    #         if sum>maxi and count==3:
    #            maxi=sum
    # print(maxi)


#     for negativ enaclues
    arr = [-4, -5, -3, -2, -9]
    maxi = 0
    l = 3
    for i in range(0, l):
        maxi += arr[i]
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            sum = 0
            count = 0
            for k in range(i, j + 1):
                sum += arr[k]
                count += 1
            if sum > maxi and count == 3:
                maxi = sum
    print(maxi)
