if __name__ == '__main__':
    arr = [4, 5, 3, 2, 9]
    maxi=arr[0]
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            sum=0
            for k in range(i, j + 1):
                sum+=arr[k]
            if sum>maxi:
               maxi=sum
    print(maxi)

