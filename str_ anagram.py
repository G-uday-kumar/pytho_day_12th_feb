def b_sort(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
# def compare_arrays(arr1,arr2):
#     if len(arr1)!=len(arr2):
#         return False
#     for i in range(len(arr1)):
#         if arr1[i]!=arr2[i]:
#             return False
#     return True




if __name__ == '__main__':
    print("enter number")
    str1=input("enter str 1:-")
    str2=input("enter str 2:-")
    arr=[]
    brr=[]
    for ch  in str1:
        arr.append(ch)
    for ch in str2:
        brr.append(ch)
    print(arr)
    print(brr)
    arr=b_sort(arr)
    brr=b_sort(brr)
    print("after soreting")
    print(arr)
    print(brr)
    print("for comparing")
    if arr==brr:
        print("equal")
    else:
        print("not equal")
    # res=compare_arrays(arr,brr)
    # if res==True:
    #     print("its anagram")
    # else:
    #     print("its not anagram")




    # print("Check anagram or not")
    # str1=input("enter first string to check :-").lower()
    # str2=input("enter second string to check :-").lower()
    # s1=sorted(str1)
    # print(s1)
    # s2=sorted(str2)
    # print(s2)
    # if s1==s2:
    #     print("yes its anagram")
    # else:
    #     print("no its not anagram")
