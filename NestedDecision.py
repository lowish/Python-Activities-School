#Codechum
#Book Recommendation

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid age entered. Please enter a whole number for age.")
    age = None

genre = input("Enter your genre in following (adventure/mystery/fantasy/scifi): ").strip().lower()

if age is not None:
    if 8 <= age <= 12:
        if genre in ("a", "adventure"):
            print("The Adventures of Tom Sawyer")
        elif genre in ("m", "mystery"):
            print("Nancy Drew: The Secret of the Old Clock")
        else:
            print("No recommendation available")
    elif age >= 13:
        if genre in ("f", "fantasy"):
            print("Harry Potter and the Sorcerer's Stone")
        elif genre in ("s", "science fiction", "scifi", "science-fiction"):
            print("Ender's Game")
        else:
            print("No recommendation available")
    else:
        print("No recommendation available")


#Senior Citizen Discount

age = int(input("Enter your age: "))
income = float(input("Enter your income:$ "))

if age >= 60 and income < 10000:
    print("Eligible for senior citizen discount")
elif age >= 60 and income >= 10000:
     print("Not eligible for senior citizen discount")
else: 
    print("Not eligible for senior citizen discount")


#Oddly or Evenly

num = int(input("Enter an integer: "))

if num % 2 == 0: 
    print("Even number")
else:
    print("Odd number")


#Exam Result Comparison

score1 = float(input("Enter the first score: "))
score2 = float(input("Enter the second score: "))

if score1 > score2 and score1 > 80:
    print("Excellent!")
elif score1 > score2 and score1 <= 80:
    print("Good Job!")
else: 
    print("Keep up the good work!")


#Second Perfection

num = int(input("Enter an integer: "))

cube_root = round(num ** (1/3))

if cube_root ** 3 == num:
    if cube_root % 2 == 0:
        print("Perfect in even cubes")
    else:
        print("Perfect in an odd way")
else: 
    print("Perfect in every way")