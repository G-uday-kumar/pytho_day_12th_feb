for i in range(1,11):
    print(i)
#even numbers

print("\nEven numbers in between the 1-20")
for i in range(1,20):
    if i%2==0:
        print(i)
#sum of first n numbers
print("Sum of first N numbers")
N=10
sum=0
for i in range(N):
    sum+=i
print("sum = "+str(sum))