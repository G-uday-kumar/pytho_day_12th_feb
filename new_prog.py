# 1️⃣ Count Digits
def count_digits(num):
    count = 0
    if num == 0:
        return 1
    while num > 0:
        num = num // 10
        count += 1
    return count


# 2️⃣ Sum of Digits
def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10
    return total


# 3️⃣ Largest Digit
def largest_digit(num):
    largest = 0
    while num > 0:
        digit = num % 10
        if digit > largest:
            largest = digit
        num = num // 10
    return largest


# 4️⃣ Prime Check
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# 5️⃣ Power Function
def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result


# 6️⃣ Armstrong Number Check (3-digit version)
def is_armstrong(num):
    original = num
    total = 0

    while num > 0:
        digit = num % 10
        total += digit ** 3
        num = num // 10

    return total == original


# ---------------------------
# 🔹 Main Section
# ---------------------------

print("Count Digits:", count_digits(12345))
print("Sum of Digits:", sum_of_digits(123))
print("Largest Digit:", largest_digit(5392))
print("Is Prime:", is_prime(7))
print("Power:", power(2, 3))
print("Is Armstrong:", is_armstrong(153))