import functools

numbers = [1, 2, 3, 4]

product = functools.reduce(lambda x, y: x * y, numbers)
print("Product of list elements:", product)