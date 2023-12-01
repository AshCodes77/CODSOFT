import random

# characters which is usable for generating password
chars ="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_-#@$%;"
length= int(input("enter length: "))
password=""

# prompt the user for the desired password length
try:
    password_length = int(input("Enter the desired length of the password: "))
except ValueError:
    print("Please enter a valid integer for the password length.")
    exit()

for a in range(length):
    password+=random.choice(chars)

#display password
print(password)
