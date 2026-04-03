def lin_serach(num):
    l=[22,23,34,45,45,56,67]
    for i in range(0, len(l)):
        if l[i] == key:
            return i

    return -1

if __name__=="__main__":

    key=int(input("enter key to search :-"))
    res=lin_serach(key)
    if res==-1:
        print("element not found so the result is :-",res)
    else:
        print("element found at the index:- ",res)





