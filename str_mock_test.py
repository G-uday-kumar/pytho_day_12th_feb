
def cont(str):
    cout=0
    for ch in str:
        cout+=1
    return cout
def rev_word(st):
    count = cont(st)
    mid = count // 2
    first = st[:mid]
    second = st[mid:]
    return first[::-1] + second[::-1]
if __name__ == '__main__':
    str="dhee coding lab"
    res=""
    rev=""
    for ch in str:
        if ch!=" ":
            res+=ch
        else:
            rev += rev_word(res) + " "
            res = ""

    rev += rev_word(res)

    print(rev)