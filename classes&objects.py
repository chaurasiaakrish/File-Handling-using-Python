# "open("name",'w')" : Is the built in function which return file objects
# "f" :  that file object is stored in the variable "f" which is called as file handler 
# A file object variable is just a variable that points to an opened file.
f=open('txt_name','r')
print("File name is:",f.name)
print("Encoding is:",f.encoding)
print("Mode is:",f.mode)
print("Is file closed ?:",f.closed)
# using f.close you cvan close your file but f.closed wil return BOOLEAN VLAUE
# weather file is close or not 
f.close()
print("Is file closed ?:",f.closed)