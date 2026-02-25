import os
path=input() #/home/akrish-chaurasia/PYTHON /FILE HANDLING/
new_name=("Enter the name you want to give :")
# path=path.replace("\\","/")
# print(path)
print (os.listdir(path)) #os.listdir(path_name) helps in listing down the files present in that path or directory
for files in os.listdir(path):
    old_name=path+files
    new_name=path+new_name+str(files)
    
# code is actually wrong somewhere 