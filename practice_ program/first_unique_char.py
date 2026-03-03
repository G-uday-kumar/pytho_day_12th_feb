def first_unique_char(s):
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    for ch in s:
        if freq[ch]==1:
            return ch
    return None
f=first_unique_char("godder_uday_kumar")
print(f)