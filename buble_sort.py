def  buble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)


if __name__=="__main__":
    print("Sorting the given list using the bubble sort function")
    arr=[32,19,21,7,3,2]
    buble_sort(arr)