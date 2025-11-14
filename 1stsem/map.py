def double(n):
    return n * 2

numbers = [5, 6, 7, 8]
result = map(double, numbers)
print(list(result))