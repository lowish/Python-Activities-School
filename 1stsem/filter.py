def is_even(n):
    return n % 2 == 0
def is_odd(n):
    return n % 2 != 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


even_numbers = filter(is_even, numbers)
odd_numbers = filter(is_odd, numbers)
print("Even numbers:", list(even_numbers))
print("Odd numbers:", list(odd_numbers))