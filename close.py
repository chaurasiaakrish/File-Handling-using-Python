# if we do not close the file explicitly then the PYTHON GARBAGE COLLECTOR will itself close 
# it automatically destroy the file and its objects.
# DO NOT RELY UPON GARBAGE COLLLECTOR
# GARBAGE COLLLECTOR will close the file after whole program will execute but due to some 
# error file may get corrupt

# THERE ARE 3 ways of closing the file:

# 1: NORMAL WAY
f=open('name','r')
# operations....
# operations....
# operations....
# operations....
f.close()
# In the middle of the program if the exception comes then program will halt and will not reach upto
# f.close() statement


# 2: Using EXCEPTION HANDLING
try:
    f=open('txt_name','r')
    # operations
    # operations
    # operations
    # operations
finally:
    f.close()    
# here which ever exception comes it will not affect the finally block as ot will always execute 


#3:Using WITH statement
with open('name','r') as f:
    print(f.read())
        # operations
     # operations 
    # operations
    # operations
# in this no matter what exception comes python explicitly will close the file 