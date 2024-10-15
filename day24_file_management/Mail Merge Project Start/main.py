with open("./Input/Names/invited_names.txt") as file_name:  # take the name and create a loop for each
    for name in file_name:  # a for loop of a .txt file will take the file line by line
        name = name.strip()  # remove space

        with open("./Input/Letters/starting_letter.txt") as file_sl:  # copy the starting letters
            starting_copy = file_sl.read()

        starting_copy = starting_copy.replace("[name]", f"{name}")  # replace [name] with the name

        with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as file:  # create a .txt file with the name as filename
            file.write(starting_copy)

    # with open(f"./Output/ReadyToSend/{name}.txt", mode="r") as file:  # manual check if necessary
    #     print(file.read())




#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp