# MA, Loops Notes

count = 1

while count <= 10:
    print(count)
    count += 1 

ducks = 1
goose = random.randint(1,11)

while True:
    if ducks == goose:
        break 
    print("Duck. . . ")
    ducks += 1
    print("Goose!!!")

siblings = ["Estaban jr.", "Alisangra"]
print(siblings[2])
name = input("What is your name: ")
siblings.append(name)
siblings.insert(1, Malaki)
print(siblings)
siblings.pop(2)
print(siblings)

for sibling in siblings:
    print(sibling)

# For Loops
for num in range(1,25):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)