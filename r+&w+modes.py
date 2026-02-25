# r+ mode:
# It helps in reading the data and then writing the data by appending and not overwriting on it
# Initially the file pointer will be at 0 and after the last character read the append operation starts 
# If the file does not exist it will throw error.

# w+ mode:
# It helps in writing the data and then reading the data.
# It opens the file and truncates it first
# If the file does not exist it will create a new one.

with open('txt_name',mode='r+') as file:
    file.read() #after reading the file pointer is at the end and from there the write method will start
    print(file.tell()) #after reading 48
    file.write("\nr+ content:This is the new content which is written after reading the file")
    print(file.tell()) # #after writing 123


with open('w+content',mode='w+') as files:
    files.write("w+ content:This is the new content which is written.And with the help of seek(0) the pointer will come at 0 and read")
    data=files.read()
    print(data)    
    #the data will not be printed beacuse the poiter is at the end
    print(files.tell()) #52 that is at the end
    # to read use seek() method
    files.seek(0)
    data=files.read()
print(data)