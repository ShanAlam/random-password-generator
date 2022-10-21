import random

# Header
print("Welcome to the Random Password Generator! \n")

# List of charecters to be used in password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Questions to be asked
num_letters= int(input("How many letters would you like in your password?\n")) 
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

# Choosing random charecters and placing them in a list
ordered_password = []

for i in range(0, num_letters):
  ordered_password.append(random.choice(letters))

for i in range(0, num_symbols):
  ordered_password.append(random.choice(symbols))

for i in range(0, num_numbers):
  ordered_password.append(random.choice(numbers))

# Randomising the order of the charecters in the password
# You could use random.shuffle() for this if you want
jumbled_password = ""

for i in range(0, len(ordered_password)):
  choice = random.choice(ordered_password)
  ordered_password.remove(choice)
  jumbled_password += choice

# Printing generated password on screen
print(f"The random password generated for you is: {jumbled_password}")
  