
lis=[23,23,66,22,28,44,35,66,77,89,98]
even_count=0
sum=0
for i in range(0,len(lis)):
    if lis[i]%2==0:
        sum=sum+lis[i]
        even_count=even_count+1

avg=sum/even_count
print(avg)
print(even_count)
print(sum)