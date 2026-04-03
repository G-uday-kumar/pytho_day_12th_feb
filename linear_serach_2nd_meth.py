if __name__=="__main__":
    l = [22, 23, 34, 45, 45, 56, 67]
    key=670
    index=-1
    for i in range(0, len(l)):
        if l[i] == key:
            index=i
            break
    print(index)
