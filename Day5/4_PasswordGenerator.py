letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random
# Simpler Approach (Sequential)
password = ""
for n in range(0,nr_letters):
    index = random.randint(0, len(letters)-1)
    password += letters[index]
for n in range(0,nr_symbols):
    index = random.randint(0, len(symbols)-1)
    password += symbols[index]
for n in range(0,nr_numbers):
    index = random.randint(0, len(numbers)-1)
    password += numbers[index]
print(password)

# Complex Approach (Random)
password_list = []
for n in range(0,nr_letters):
    index = random.randint(0, len(letters)-1)
    password_list.append(letters[index])
for n in range(0,nr_symbols):
    index = random.randint(0, len(symbols)-1)
    password_list.append(symbols[index])
for n in range(0,nr_numbers):
    index = random.randint(0, len(numbers)-1)
    password_list.append(numbers[index])

random.shuffle(password_list)
password_string = ""
for char in password_list:
    password_string += char

print(password_string)

#Method 3 (Optimised)
password_list = (
        random.choices(letters, k=nr_letters) +
        random.choices(symbols, k=nr_symbols) +
        random.choices(numbers, k=nr_numbers)
    )
random.shuffle(password_list)
print(''.join(password_list))