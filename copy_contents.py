# First Method
with open('writeONfile','r') as file1:
    data = file1.read()
with open('copy_content1','w') as file2:
        file2.write(data)

# Second Method
file1=open('writeONfile','r')
file2=open('copy_content2','w')
for i in file1:
    file2.write(i)
file1.close()
file2.close()    
