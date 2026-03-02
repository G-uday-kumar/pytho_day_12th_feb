
#  write a prog to count the no of ovels in a given str
str=input('enter the string values to count the vowels:-')
count=0
i=0

while i<len(str):
    if str[i] in 'AEIOUaeiou':
        count+=1
    i+=1
print("no. of vowels:",count)
