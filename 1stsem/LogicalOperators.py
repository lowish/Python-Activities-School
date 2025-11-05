#Codechum
#Number is Positive and Even

num = int(input("Enter an integer: "))

print("Is the number positive and even?")

if (num > 0 and num % 2 == 0):
    print("Yes")
else:
    print("No")
    

#Comfortable Temperature

num = int(input("Enter an integer: "))

print("Is the number positive and even?")

if (num > 0 and num % 2 == 0):
    print("Yes")
else:
    print("No")


#Is The Letter a Lowercase Consonant?

lower = input("Enter a lowercase letter: ")

print("Is it a lowercase consonant?")

if len(lower) == 1 and 'a' <= lower <= 'z':
    print("Yes")
else:
    print("No")


#Is Number Outside All Target Ranges?

num = int(input("Enter an integer: "))

if not (10 <= num <= 20 or 30 <= num <= 40 or 90 <= num <= 100):
    print("Outside all target ranges")
else:
    print("Within at least one target range")


#Password Validator with Multiple Criteria

put = input("Enter a password: ")

if len(put) != 8:
    print("Password must be exactly 8 characters")
    
elif not('a' <= put[0] <= 'z'):
    print("Password must start with a lowercase letter") 
    
elif '@' not in put:
    print("Password must contain '@'")
    
elif ' ' not in put:
    print("Password must not contain spaces")
    
else: 
    print("Password is valid")