#Codechum
#Digit Count

num = int(input("Enter a positive integer: "))

temp = num
count = 0

while temp > 0:
    temp = temp // 10
    count += 1
    
print("Number of digits:", count)


#While loop counting

num = int(input("Enter a number: "))

i = 0

while i <= num:
    print(i)
    i += 1


#Even Number Printer

num = int(input("Enter a positive integer: "))

i = 2
while i <= num:
    print(i)
    i += 2


#Square Numbers

num = int(input("Enter a number: "))

i = 1
while i <= num:
    print(i * i)
    i += 1


#Sum of Digits

num = int(input("Enter an integer: "))

sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    
    sum += digit
    
    temp //= 10
print("Sum of digits:", sum)