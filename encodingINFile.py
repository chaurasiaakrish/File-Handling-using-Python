# Disk → Bytes → (Encoding) → Characters


# Text files: go all the way
# Binary files: stop at bytes
# Encoding is the rule that converts bytes into human-readable characters,
#  which is required for text files but irrelevant for binary files.

#This is the case in binary mode 
file=open('/home/akrish-chaurasia/Downloads/Condensed_Resume.pdf','rb')
for i in file :
    print ("This the content of binary file",i)


# This is the case in Text files 
with open('txt_name','r') as f:
    print ("This is the content of text file",f.read())