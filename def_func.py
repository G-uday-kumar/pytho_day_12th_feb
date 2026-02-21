# 1️⃣ Write function to check even or odd
# def is_even(num):
#     # return True or False
def is_even(num):
    if num%2==0:
        return True
    else:
        return False
print("the result is :-",is_even(5))
# 2️⃣ Function to find largest of 3 numbers
def greatest_of_3(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1,"is greater"
    elif n2>n1 and n2>n3:
        return n2, "is greater"
    else:
        return n3,"is greater"
print(greatest_of_3)

# 3️⃣ Reverse a Number
def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev


# 4️⃣ Palindrome Check
def is_palindrome(num):
    return num == reverse_number(num)


# 5️⃣ Factorial
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print("Even check:", is_even(4))
print("Largest:", largest(10, 25, 5))
print("Reverse:", reverse_number(123))
print("Is Palindrome:", is_palindrome(121))
print("Factorial:", factorial(5))
# 4️⃣ Function to check palindrome number
# 5️⃣ Function to calculate factorial