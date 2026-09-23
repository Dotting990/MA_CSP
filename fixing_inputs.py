# MA, Fixing user inputs
while True:
    color = input("Tell me a color that is only one word: ").strip().capitalize()
    if color.isnumeric():
        print("That is a number not a color!")
    elif " " in color:
        print("One word.")
    else:
        break
print(f"we painted the walls {color}!")