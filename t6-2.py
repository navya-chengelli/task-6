def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Count prime numbers and create a new list
prime_numbers = [num for num in numbers if is_prime(num)]

print("Prime numbers:", prime_numbers)




