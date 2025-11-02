#Codechum
#Difference of Digits

n = input("Enter a positive integer: ")

result = int(n[-1])

for i in range(len(n) -2, -1, -1):
    result -= int(n[i])
    
print("Result of subtracting digits:", result)


#For loop Counting

n = int(input("Enter a positive integer: "))

for i in range(1, n + 1):
    print(i)


#Multiplication of 5 

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i * 10)


#Odd number printer

n = int(input("Enter a positive integer: "))

for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)


#A's and B's

s = input("Enter a string: ")

count_a = 0
count_b = 0

for ch in s:
    if ch == 'a':
        count_a += 1
    elif ch == 'b':
        count_b += 1
print("Number of 'a' occurrences:", count_a)
print("Number of 'b' occurrences:", count_b)


