def is_palindrome_string(s):
    i=0
    j=len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
        
    return "its pallendrom"
p=is_palindrome_string("racecar")
print(p)
