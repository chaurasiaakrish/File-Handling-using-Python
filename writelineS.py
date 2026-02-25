# writelines(): A method which is used to write the group of lines of strings into the file represented by a file object
# Group of strings are stored in the form of lists ,tuples or sets

# syntax: file_object.writelines(set/list/tuple)
# mode: w

l=["Akrish \n","Chaurasia \n","B.Tech","3rd year \n","Abesit \n","Ghaziabad"]
with open('txt_name','w') as file:
    file.writelines(l)