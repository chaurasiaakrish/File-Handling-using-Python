f=open("name",'w')
if  not f:
    print ("File found successfully ")
print (type(f))    
# <class '_io.TextIOWrapper'> is the data type of the file

# Suppose if the file is not the cdir so path name should also have to be mentioned before the file name 
# open("/home/akrish-chaurasia/Downloads/Condensed_Resume.pdf", "rb")
file=open('/home/akrish-chaurasia/Downloads/Condensed_Resume.pdf','rb')
for i in file :
    print (i)