if __name__ == '__main__':
    arr=[12,23,12,12,23,23,24,45]
    dict={}
    for key in arr:
        if key in dict:
            dict[key]=dict[key]+1
        else:
            dict[key]=1
    print(dict)
    print("DUplicate values in the dictionary")
    for key in dict:
        if dict[key]>1:
            print(key)
    print("Unique values in the dictionary")
    for key in dict:
        if dict[key]==1:
            print(key)
    print("Duplicate values frequency in the dictionary")
    for key in dict:
        # if dict[key]>1:
        print(key,":",dict[key])

    print("REmove duplicate values in the Array")
    # arr1 = [12, 23, 12, 12, 23, 23, 24, 45]
    res=[]
    for ele in arr:
        if ele not in res:
            res.append(ele)
    print(res)

