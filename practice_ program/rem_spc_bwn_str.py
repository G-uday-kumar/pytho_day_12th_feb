str=input('enter the string values:-')
new_str=""
i=0
while i<len(str):
    data=str[i]
    if data == " ":
        i=i+1
    else:
       new_str+=data
       i+=1
print(new_str)



