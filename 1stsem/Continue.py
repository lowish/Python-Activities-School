#Codechum
#Prime Factor

num = int(input("Enter a number: "))
print(f"Prime factors of {num} (excluding multiples of 3): ", end="")

i = 2
factors = []

while i <= num:
    if num % i == 0:
        if i % 3 == 0:
            i += 1
            continue
        if i not in factors:
            factors.append(i)
            print(i, end=" ")
        num //= i
    else:
        i += 1


#Skipping Number

num = int(input("Enter a number: "))
for x in range(1, num + 1):
    if x == 4:
        continue
    print(x, end=" ")


#Average Calculation

total = 0
count = 0

while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    if num < 0:
        continue
    total += num
    count += 1
    
if count > 0:
    average = total / count
    print(f"Average: {average:.2f}")
else:
    print("No valid numbers entered.")


#Sum of NonNegative Number

total = 0

while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    if num < 0:
        continue
    total += num
print(f"Sum: {total}")


#Printing Even Numbers with Skip

limit = int(input("Enter a number: "))
printed = False

for x in range(0, limit + 1, 2):
    if x == 10:
        continue
    print(x, end=" ")
    printed = True
    
if not printed:
    print("No even number to display")