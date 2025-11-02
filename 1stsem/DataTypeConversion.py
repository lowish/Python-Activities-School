#Codechum 
#Type Conversion Difference

num1 = int(input("Enter an Integer: "))
num2 = float(input("Enter a Float: "))


difference = num1 - num2

print(f"The difference is:{difference:.2f}")


#ASCII Sum

x = input("Enter first character: ")
y = input("Enter second character: ")

print("Sum:", ord(x) + ord(y))


#Float to String Conversion

string_number = input("Enter a string containing a float: ")

result = float(string_number)

print(f"Floating-point number: {result:.2f}")


#Lesser Character

char1 = str(input("Enter character 1: "))
char2 = str(input("Enter character 2: "))

if char1 < char2:
    print("The lesser character is:", char1)
else: 
    print("The lesser character is:", char2)


#String to Integer

var = input("Enter a string: ")

integer = int(var)

print(f"String converted to integer: {integer}")

