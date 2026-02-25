# tell() method helps in telling the current postion the cursor or file pointer is after every read() of the file 
# Syntax: file_object.tell()

# seek() method helps in changing the position of the pointer of the file pointer 
# Syntax: file_object.seek(position)
# position will take you to that indicated position 

# file pointer position is always counted from the beginning and starts with 0

with open('txt_name','r') as f:
    print(f.tell()) 
    # initially pointer is at 0 
    print(f.read(3))
    print(f.tell())
    # now pointer is at 3
    f.seek(0)
    # pointer set to 0 agian 
    print(f.read(7))
    # since pointer set to 0 again so it read 7 characters from 0 to 7
    print(f.tell())