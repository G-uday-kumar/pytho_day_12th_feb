
# prog to reverse a str without using slice operator
s=input("enter the str:-")
i=len(s)-1
rev_str=""
while i>=0:
    rev_str+=s[i]
    i=i-1
print(rev_str)