# the volatile way of creating a file to take input and when turned off gets erased 
# age=int(input("Enter the age to check"))
# if age>18:
#     print("Eligible to vote")
# else:
#     print ("Not eligible to vote")    

# FILE HANDLING HELPS IN CRETAING A FILE WHICH IS NON_VOLATILE

age=input("Enter the age to check ")
f=open("name",'w')
# chnage in the name o the file will lead to change in the creation of new file
f.write(age)
f.close()