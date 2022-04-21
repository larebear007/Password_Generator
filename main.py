# Password Generator

# Your password should be at least 12 characters long.
# Password should consist of lowercase and uppercase letters, numbers and symbols.

import random
import string

# List of characters to pull from
chars = string.punctuation + string.digits + string.ascii_uppercase + string.ascii_lowercase
bad_chars = '{}[]()/\\\'"`~,;:.<>'
chars_list = []
for char in chars:
    if char in bad_chars:
        continue
    chars_list.append(char)


print('Welcome to Password Generator!')
while True:
    amount = input('How many passwords would you like to make? ')
    length = input('How long would you like each password to be? ')
    if amount.isnumeric() and length.isnumeric():
        amount = int(amount)
        length = int(length)
        password = None
        for idx in range(amount):
            pass_list = random.choices(chars_list, k=length)
            password = ''.join(pass_list)
            print(idx + 1, password)
        break

    else:
        print('Please enter a number for the amount of passwords and the length of the password.')

