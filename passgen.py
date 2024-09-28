from passkeys import letters, symbols, numbers
import random

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("number of letters you like in you passkey?\n"))
nr_symbols = int(input(f"number of symbols you like to be in your passkey?\n"))
nr_numbers = int(input(f"numericals you like to be in your passkey?\n"))

passkey = []
for letter in range(1, nr_letters + 1):
    passkey.append(random.choice(letters))

for symbol in range(1, nr_symbols + 1):
    passkey.append(random.choice(symbols))

for number in range(1, nr_numbers + 1):
    passkey.append(random.choice(numbers))

random.shuffle(passkey)

final_passkey = ""
for key in passkey:
    final_passkey += key

print(f"Your passkey is : {final_passkey}")