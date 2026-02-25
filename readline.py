# readline method 
# This method helps in reading the file line by line 
# SYNTAX :   .readline()


with open('txt_name','r') as f:
    data=f.readline()
    print (data,end="")
    # now the pointer will be after the last word read in data
    data1=f.readline(21)
    print (data1)

    # Hello I am Akrish Chaurasia

    # I am doing graduation 
    # from ABESIT in BTECH(CSE) is not included as 21 words were only included in the ''data1''
# this is the output which we got and it has a new line which is beacuse of \n which is being created by print and the 
# textfile itself had one new line 

# to overcome the /n of print we can use th keyword end=""