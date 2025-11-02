#Codechum
#List Remove Consecutive Duplicates

input_str = input("Enter list of integers: ")
input_list = [int(x) for x in input_str.split()]

def remove_consecutive_duplicates(input_list):
    if not input_list:
        return []
        
    result = [input_list[0]]
    for x in range(1, len(input_list)):
        if input_list[x] != input_list[x-1]:
            result.append(input_list[x])
    return result
    
remove_list = remove_consecutive_duplicates(input_list)
print(f"List with consecutive duplicates removed: {remove_list}")


#Maximum  Product of Two Integers

numbers_str = input("Enter the numbers separated by space: ")
numbers = list(map(int, numbers_str.split()))

numbers.sort()

max_product = numbers[-1] * numbers[-2]

print(f"Maximum Product: {max_product}")


#Odd numbers

n = int(input("Enter an integer: "))


odd = []

for i in range(n + 1):
    if i % 2 != 0:
        odd.append(i)

print(odd)


#Vowels

text = input("Enter a string: ")

vowels ="aeiouAEIOU"

vowel_list = [ch for ch in text if ch in vowels]

print(vowel_list)


#Even or Odd Comprehension

n = int(input("Enter a number: "))

labels = []

for i in range(1, n + 1):
    if i % 2 == 0:
        labels.append('even')
    else:
        labels.append('odd')

print(labels)