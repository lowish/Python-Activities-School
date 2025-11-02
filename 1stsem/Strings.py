#Prince Tan
# ICT107

#Part1

word = "Python"

print("Characters in the string:")
for char in word:
    print(char)

# c Print the length of the string using len()
print("Length of the string:", len(word))

#Part2

first_name = "John"
last_name = "Smith"

full_name = first_name + " " + last_name
print("Full name:", full_name)

#Part3 

word = "Python"

new = "J" +  word[1:]
print("New word:", new)

#Part4

word = "Programming in Python"

print(word[0:7]) 
print(word[-6:])  
print(word[3:14])  
print(word[::2])  
print(word[::-1]) 

#Part5

message = "  python programming is fun!  "

print(message.upper())
print(message.title())
trim_message = message.strip()
print(trim_message) 
replace = trim_message.replace("fun", "awesome")
print(replace)
count_p = replace.count("p")
print(count_p)
starts_with_python = replace.startswith("python")
print(starts_with_python)
index_programming = replace.find("programming")
print(index_programming)
print(replace)


#Part6

full_name = input("Enter your full name: ")

no_spaces = full_name.replace(" ", "")
print("Number of characters (excluding spaces):", len(no_spaces))

parts = full_name.split()
if len(parts) > 1:
    initials = parts[0][0].upper() + "." + parts[-1][0].upper() + "."
else:
   
    initials = parts[0][0].upper() + "." + parts[0][0].upper() + "."
print("Initials:", initials)

print("reverse name:", full_name[::-1])

print("message:", "Hello, " + full_name.title() + "!")