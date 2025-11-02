#Codechum 
#Mulplication Table

num = int(input("Enter an integer: "))

print("Multiplication Table")

table = []
i = 0
while i < num:
    row = []
    j = 0
    while j < num:
        row.append(0)
        j += 1
    table.append(row)
    i += 1

i = 0
while i < num:
    j = 0
    while j < num:
        table[i][j] = (i + 1) * (j + 1)
        j += 1
    i += 1

i = 0
while i < num:
    j = 0
    while j < num:
        print(table[i][j], end="\t")
        j += 1
    print()
    i += 1


#Alphabet Triangle Pattern 

n = int(input("Enter the number of rows: "))

ch = 65

for e in range (1, n + 1):
    for j in range(1, e + 1):
            print(chr(ch), end=" ")
            ch += 1
    print()


#Reversed Right  Triangle 

num = int(input("Enter a number: "))

for z in range (1, num + 1):
    for t in range(num - z):
        print(" ", end="")
        
    for s in range(z):
        print(z, end="")
    print()


#Character Pattern with Alternating Rows

firstChar = input("Enter First Character: ").strip()
secondChar = input("Enter Second Character: ").strip()
size = int(input("Enter Size: ").strip())

if firstChar:
    firstChar = firstChar[0]
if secondChar:
    secondChar = secondChar[0]

i = 0
while i < size:
    j = 0 
    while j < i:
        print("-", end="")
        j+= 1

    if i % 2 == 0:
        print(firstChar)
    else:
        print(secondChar)
    i += 1


#Numbered Triangle

n = int(input("Enter an integer: "))

for z in range (1, n + 1):
    for j in range(1, z + 1):
        print(j, end=" ")
    print()