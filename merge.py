l=[]
files=input("Enter the name of the file to merge: ")
l.append(files)
while True:
    response=input("Do you want to add more files: y/n ").lower()
    if response!='y':
        break
    else:
        files=input("Enter the name of the file to merge: ")
        l.append(files) 
# for i in l:
#     i+'.txt'                  
# print(l)        
for i in l:
    with open(i+'.txt',mode='r') as file:
        data=file.read()
    with open('merged_files','a') as merge: # a helps in appending the contents to the file without overwriting on it
        merge.write(data)  