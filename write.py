# if the file exists it will write there and if no file exists
#  then will create a new file to write the contents 
# if file didn't existed then read() threw errors

# mode:
# w:To write only and it overwrites to the file
# a:
# x:

# write() and writelines()
# syntax: file_variable.write("Data in string format")

with  open('writeONfile','w') as file:
    file.write("This is the content which have written on the new file created here in this open () only")
    # when we run the program for the first time the curosr will be at the beginning of the file
    # but during the exectuion of the program the cursor changes the position accordingly 

# w returns the no.of charcters it has overwritten (integer value)