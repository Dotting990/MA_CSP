# MA, Password Strength Checker
Password = input("What is your password: ")
length = False 
uppercase = False
lowercase = False
number = False  
symbol = False
for letter in Password:
    if len(Password) >= 8:
        length = True

for letter in Password:
    if letter.isupper():
        uppercase = True

for letter in Password:
    if letter.islower():
        lowercase = True

for letter in Password:
    if letter.isnumeric:
        number = True

