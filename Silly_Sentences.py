# MA, 7th, Silly Sentences
while True:
    verb = input("Tell me a verb ending in ing: ")
    if verb.isnumeric(ing):
        print("That does not have ing at the end")
    elif " " in verb:
        print("One word please")
    else:
        break
    place = input("Tell me a place: ")
    color = input("Tell me a color: ")
    travel = input("Tell me a way to travel: ")
    emotion = input("Tell me an emotion: ")
    animal = input("Tell me an animal: ")

