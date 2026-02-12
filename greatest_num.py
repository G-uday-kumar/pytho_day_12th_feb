a = 10
b = 122
c = 121

if a > b and a > c:
    print("a is greater")
elif b > a and b > c:
    print("b is greater")
else:
    print("c is greater")
largest = max(a, b, c)
print("large is: " + str(largest))
