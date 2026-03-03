def count_vowels(s):
    count=0
    for ch in s:
        if ch in "AEIOUaeiou":
            count+=1
        
    return count
d=count_vowels("Education")
print("the number of vowels are",d)