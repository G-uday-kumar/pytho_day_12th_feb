def clock_wise(arr):
    temp=arr[len(arr)-1]
    for i in range(len(arr)-1,-1,-1):
        arr[i]=arr[i-1]
    arr[0]=temp
    print(arr)
if __name__ == '__main__':
    arr=[1,2,3,4,5,6]
    clock_wise(arr)