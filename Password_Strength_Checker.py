# MA, Password Strength Checker
Password = input("What is your password: ")
length = False 
uppercase = False
lowercase = False
number = False  
symbol = False
for letter in Password:
    if letter.isupper():
        uppercase = True