#Codechum
#Squaring the Years

year = int(input("Enter your birth year: "))
current = int(input("Enter the current year: "))

subtract = year - current
square_root = subtract  ** 0.5

if square_root == str(square_root):
    print("Your age is a perfect square.")
else:
    print("Your age is not a perfect square.")


#Capricorns Now

month = int(input("Enter your birth month: "))
day = int(input("Enter your birth day: "))

if (month == 12 and day == 22) or (month == 1 and day <= 19):
    print("Your zodiac sign is Capricorn.")
else:
    print("Your zodiac sign is not Capricorn.")


#Voting Age

age = int(input("Enter your age: "))

if (age >= 18):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


#Alphabet Category

age = int(input("Enter your age: "))

if (age >= 18):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


#Equal Numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 == num2 & num1 == num3: 
    print("All numbers are equal.")
else: 
    print("Not all numbers are equal.")
