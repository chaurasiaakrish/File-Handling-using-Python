# readlines() method 
# This method helps in redaing the contents of the file word by word 
with open('txt_name','r')as f:
    # print (f.readlines(),end=" ")  /n will occur 
    for i in f:
        print (i,end="")