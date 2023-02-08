# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

print("")
# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password = ""
hard_password = []
for char in range(1, nr_letters + 1):
    letters_choice = random.choice(letters)
    # password += letters_choice
    hard_password.append(letters_choice)

for sym in range(1, nr_symbols + 1):
    symbols_choice = random.choice(symbols)
    # password += symbols_choice
    hard_password.append(symbols_choice)

for i in range(1, nr_numbers + 1):
    numbers_choice = random.choice(numbers)
    # password += numbers_choice
    hard_password.append(numbers_choice)

print(hard_password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random.shuffle(hard_password)
print(hard_password)

password = ""

for char in hard_password:
    password += char

print(password)
