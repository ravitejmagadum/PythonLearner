#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


f = open("Input/Names/invited_names.txt", "r")
i = 0
for x in f:
    new_letter = open(f"Output/ReadyToSend/letter{x.strip()}.txt", 'a')
    new_letter.write(f"Dear {x.strip()},")
    i+=1
    copy_letter = open("Input/Letters/starting_letter.txt", 'r')
    greet = copy_letter.readline()
    new_letter.write(copy_letter.read())

