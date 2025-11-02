#Codechum
#All or Not

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))


if num1 > 0 and num2 > 0 and num3 > 0:
    print("All numbers are positive.")
elif num1 < 0 and num2 < 0 and num3 < 0: 
    print("All numbers are negative.")
elif num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0:
    print("All numbers are even.")
elif num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 != 0:
    print("All numbers are odd.")
else: 
    print("Numbers are different.")


#Divisible by

num = int(input("Enter an integer: "))

if num % 4 == 0:
    print("The number is divisible by 4.")
elif num % 3 == 0:
    print("The number is divisible by 3.")
elif num % 2 == 0:
    print("The number is divisible by 2.")
else:
    print("The number is not divisible by 2, 3, or 4.")

#Day Identifier

day = int(input("Enter number 1 to 7 to identify, what is day?: "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid input")


#Positive,Negative, or Zero Counter

positive = 0
negative = 0
zero = 0

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))
num4 = int(input("Enter fourth integer: "))
num5 = int(input("Enter fifth integer: "))

number = [num1, num2, num3, num4, num5]

for i in number:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
    else:
        zero += 1
        
print("Positive count:", positive)
print("Negative count:", negative)
print("Zero count:", zero)

#What year is it?

year = int(input("Enter a year: "))

if (year % 100 == 0): 
    if (year % 400 == 0):
        print("It's a leap century year.")
    else:
        print("It's a century year.")
elif (year % 4  == 0):
    print("It's a leap year.")
else:
    print("It's neither a leap year nor a century year.")