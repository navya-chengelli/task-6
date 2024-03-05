def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

def count_happy_numbers(numbers):
    count = 0
    for num in numbers:
        if is_happy_number(num):
            count += 1
    return count
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
happy_count = count_happy_numbers(numbers)
print("Number of happy numbers:", happy_count)
print("[",numbers[0],",",numbers[4],"]")