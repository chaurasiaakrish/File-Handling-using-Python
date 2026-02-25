# w mode was overwriting the existing file contents 


# x mode will check wether the file  specified exists or not if yes then it will produce error
# and if the file not exists then only it will execute in cretaing and writing the contents to the file 

# with open('txt_name','x') as file:
#     file.write("This will produce error as the file already exists")

with open('X_mode','x') as file:
    file.write("This will create a new file and will write these contents to it")  

# if programs re-run then error will produce as file already created once.

# Advantage is old files will be protected from getting overwritten