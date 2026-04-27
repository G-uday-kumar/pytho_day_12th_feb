def f_uper(cr):
    res=""
    for i in range (0,len(cr)):
        if i==0 and ord(cr[i])>=97 and ord(cr[i])<=122:
            res=res+chr(ord(cr[0])-32)
        else:
            res=res+cr[i]
    return res
def reverss(cr):
    res=""
    for i in range (len(cr)-1,-1,-1):
        res=res+cr[i]
    return res


if __name__ == '__main__':
    str1="dhee coding lab"
    str2=str1.split(" ")
    print(str2)
    for key in str2:
        print(key, end=" ")
    print()
    # print("first letter caps")
    for ele in str2:
        print(f_uper(ele), end=" ")
    print()
    # print("reverse  the each letters in each words")
    for ele in str2:
        print(reverss(ele), end=" ")
    print()
    # print("")
    for  ele in str2:
        print(f_uper(reverss(f_uper(ele))), end=" ")
    print()
    for ele in str2:
        print(f_uper(reverss(ele)), end=" ")
    print()
    for i in range(len(str2)-1,-1,-1):
        print(f_uper(str2[i]), end=" ")












     # for key in str2:
     #     print(key, end=" ")