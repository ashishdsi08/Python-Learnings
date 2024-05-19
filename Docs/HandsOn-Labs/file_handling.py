
try:
    file = open("file1.txt",'r')
    print(file.read())
    print(file.readline())


    for x in file:
        print(x)
finally:
    file.close()


"""
Loop over a directory structure
"""

# importing os module  
import os 
   
# Get the path of current working directory 
path = os.getcwd() 
   
# Get the list of all files and directories 
dir_list = os.listdir(path) 
   
for file in dir_list:
  if os.path.isdir(file):
    print("Is a Directory : ", file)
  else:
    print("Is a file : ", file)

"""
https://www.geeksforgeeks.org/reading-csv-files-in-python/

"""
import csv

with open('EmployeeData.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        print(lines)

"""
to install pandad
pip install pandas 
import pandas
csvFile = pandas.read_csv('Giants.csv')
print(csvFile)
"""

    