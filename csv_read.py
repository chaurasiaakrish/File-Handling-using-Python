# csv stands for comma seperated values
# these are the files which are in the form of tabular form or in any delimeter format
# import csv is the module to be imported for the reading and writing purpose of the ccsv file 

import csv 
with open('data_cleaning_method2.csv') as f:
    pdf=csv.reader(f,delimiter=',') #stores the object at some memory location <_csv.reader object at 0x78e1abc56500>
    print(pdf) # help in printing the memory location
    # to see the contents if the csv file use for loop
    for i in f:
        print(i,end='')
# for working with csv files pandas and somewhat numpy are the best..
