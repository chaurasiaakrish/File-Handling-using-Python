# # to count the no.of words in a particular file 
# # to count the no.of lines in a particular file 
# # to count the no.of characters in a particular file 

with open('name','r') as file:
    number_of_words=0
    number_of_lines=0
    number_of_characters=0
    for lines in file:
        number_of_characters+=len(lines.strip())
        number_of_lines+=1
        number_of_words+=len(lines.strip().split())
    print ("number_of_characters=",number_of_characters)    
    print("number_of_lines=",number_of_lines)
    print("number_of_words=",number_of_words)

    # += is called as compound operator 
