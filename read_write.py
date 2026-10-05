# MA, Reading and Writing to Files
# To read a File
#Key words to open a file
        #The file path
             #What we do with the file
                            #Naming the file to be able to use it
# "r" stands for "read"
# "r+" lets you read AND append
with open("practice.txt", "r+") as file:
    #Gives you what is writen on the file
    content = file.read()
    content = "Chapter 1:\n" + content + "And christopher Robin was sitting on his door step putting on his big boots"
    file.write(content)

# "w" stands for Write and replaces the content
# "a" stands for append and adds content to the end
with open("practice.txt", "a") as file:
    file.write("\nWinnie the Pooh and the Blustery Day.")