# membership operator
# from operator import indexOf "IN and NOT IN" we are using
#
# if __name__=="__main__":
#     arr=[20,30,40,50]
#     key=30
#     print(key in arr)
#     print(key not in arr)
#
# # it may be use in the arr,str and all
# print("now checking for the string values")
# if __name__=="__main__":
#     str="uday_kumar_day"
#     key="day"
#     key1="y"
#     print(key1 in str)#for the char
#     print("yes the key value",key,"in ",str,key in str)# for the substr
#     a=indexOf(print(key1 in str))#


# #identity operator
# if __name__=="__main__":
#     arr = [20, 30, 40, 50]
#     arr1=[20,30,40,50]
#     print(arr is arr1)#result false bcz bothe are store in diff mem locaion
#     print(arr[0] is arr1[0])#result it as a true bcz elemnt store the in the same mem location
#     print(id(arr[0]))# both are give the same memory address
#     print(id(arr1[0]))#--||--
#     print(id(arr))#both having the different mem location
#     print(id(arr1))#--||--


# #ternary operator
#
# if __name__=="__main__":
#     a=int(input("enter number:"))
#     print("pos" if a>0 else "neg" if a<0 else "zero")

# if __name__=="__main__":
#     a=int(input("enter number:"))
#     print("pos" if a>0 else "neg" if a<0 else "zero")


if __name__=="__main__":
    arr = [20, 30, 40, 50]
    arr1=[20,30,40,50]
    arr2=arr1
    print(id(arr1) is id(arr2))
