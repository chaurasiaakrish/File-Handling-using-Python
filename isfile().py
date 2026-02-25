# This is the function of the path module which is the sub module of the os module 
# which helps in checking the existence of the file in the 
# current working directory in which the python file is also there ..

# import os 
# os.path.isfile('filename')
# this is the syntax 
# returns boolean value 


import os 
print(os.path.isfile('txt_name'))
# since txt_name was present in the present directory in which this python code is there therefore it 
# given the result as True 

print (os.path.isfile('downloads'))
# this time it will give False 