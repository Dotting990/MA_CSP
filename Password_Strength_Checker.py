# MA, Password Strength Checker
Password = input("What is your password: ")
length = False 
uppercase = False
lowercase = False
number = False  
symbol = False
count = 0
strength = "week"
if len(Password) >= 8:
    length = True
print(f"Password has at least 8 characters {length}")

for letter in Password:
    if letter.isupper():
        uppercase = True
print(f"Password has at least one uppercase letter {uppercase}")
        
for letter in Password:
    if letter.islower():
        lowercase = True
print(f"Password has at least one lowercase letter {lowercase}")

for letter in Password:
    if letter.isnumeric:
        number = True
print(f"Password has at least one number")

for  letter in Password
    if letter in "@$?!:;()/-.,&[]{}#%^*+=_\|~<>"
        symbol = true
print(f"Password has a symbol")

if length == True:
    count = count + 1
    
if uppercase == True:
    count = count + 1
    
if lowercase == True:
    count = count + 1
    
if number == True:
    count = count + 1
    
if symbol == True:
    count = count + 1

if count < 2
    print(f"Your password is Weak")
    
if count > 3 and <= 4
 print(f"Your password is Midium")

if count == 5
    print(f"Your password is Strong")
