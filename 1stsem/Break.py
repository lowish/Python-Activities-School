#Codechum
#Prime Numbers

num = int(input("Enter a positive integer: "))

if num <= 1:
    print(f"{num} is not a prime number")
else:
    prime = True
    for i in range(2, int(num ** 0.5)):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(f"{num} is prime number")
    else:
        print(f"{num} is not a prime number")


#Password Attempts

attempts = int(input("Enter a number of attempts: "))
remaining = attempts

while remaining > 0:
    print("Enter a password: ", end="")
    password = input()
    
    if password == "secret":
        print("Access granted!")
        break
    else:
        remaining -= 1
        print(f"Access denied! {remaining} attempts remaining.")
        if remaining == 0:
            print("Access denied!")


#Number Break

while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    print("Number:", num)


#Positive number sum

total = 0

while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break
    if num > 0:
        total += num
print("Sum of positive numbers:", total)


#Palindrome Checker

while True:
    word = input("Enter a word: ")
    if word == word[::-1]:
        print("Palindrome found!")
        break