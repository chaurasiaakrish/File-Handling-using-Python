# file object methods are of two types:
# readable() and writable()
# weather file readable or not and writable or not ?? Returns boolean values 


f=open('txt_name','r+')
# print (f.readable())
# print (f.writable())
# f.close()


# w+ and r+ mode help in persforming read and write operations at the same time 
# hence readable() and writable() both will give true values.

if f.mode=='r':
    print("The file is writable",f.readable())
elif f.mode =='w' or f.mode=='r+' or f.mode=='w+':
    print ("The file is writable",f.writable())    