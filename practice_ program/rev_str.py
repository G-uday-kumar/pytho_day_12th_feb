def reverse_string(s):
    rev_str=""
    i=len(s)-1
    for i in range(len(s)-1,-1,-1):
        rev_str+=s[i]
    return rev_str
d=reverse_string("uday")
print(d)