def binary_search(arr,key):
    start = 0
    end = len(arr)-1

    while start<=end:
        mid=(start+end)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            end=mid-1
        else:
            start=mid+1
    return -1



if __name__=="__main__":
    arr=[2,4,6,8,12,24,32]
    key=int(input("enter key to search:-"))
    res=binary_search(arr,key)
    if res==-1:
        print("Sorry array element not found",res)
    else:
        print("array element found at the ",res)