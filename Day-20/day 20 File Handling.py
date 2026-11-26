#FILE CREATION
file = open("students.txt","w")        # creates a writing file
file.write("hello this is Zeeshan")

file = open("students.txt","r")
data = file.read()                      # reads the file
print(data)
print()
file = open("students.txt","w")            #writes a new file and previous written file gets erasesd
new_write = ''' how are         you'''
file.write(new_write)

file = open("students.txt","r")         # prints the second file(new_write) but not 1st file(data)
print(file.read())
print()

file = open("students.txt","a")              # appends the data here it doesnt delete the previous data
append_data  = ''' welcome to programming'''
file.write(append_data)

file = open("students.txt","r")
print(file.read())
print()

file.close()      #always close the file at the end or buffer occurs


file = open("students.txt","a")
add_new_data='''\nwhich is python 
                full stack'''
file.write(add_new_data)

file = open("students.txt","r")
print(file.read())
print()

file = open("students.txt","r")
# print(file.readline()) #only 1st line



 #insted of printing new lines again and again use for loop
# for line in file:
#     print(line)
print(file.readlines()) #all lines in single line as a list
file.close()
with open("students.txt","r") as file:  # after closing a file use with open 
    for line in file:
        print(line)
print()

import csv
with open("sample.csv","w") as f1:
    data = [['name','age'],['azeem',22],['zeeshan',23]]
    writer = csv.writer(f1)
    writer.writerows(data)
    

with open("sample.csv","r") as f2:
    print(f2.read())