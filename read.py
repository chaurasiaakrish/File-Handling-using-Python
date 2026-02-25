f=open("name",'r')
file=open("txt_name",'r')
# print(f.read())
# print(file.read())
f.close()
file.close()

# in this .read() is the method which helps in reading the file
# and read("number") that much no.of characters the file wil read 
# if the no. is not specified or it is in negative the python will read the whole file
# in this case the couting satrts from 0 for reading the characters 


with open('txt_name','r') as f1:
    print (f1.read(7))
    # ''hello i'' one letter counted for space
    print (f1.read(20))
    # since the file previously counted the first 7 characters so the pointer will start from 8th to count from onwards
    # th ''new line'' and the ''space'' are considered as a word in file 