f = open("demo.txt", "r")
data = f.read()
print(data)
# basic way to write file i/o

f=open("practice.txt")
data=f.readlines()
print(type(data))

f = open("practice.txt")
data = f.readline()  #first line
while data != "":
    print(data)
    data1 = f.readline() #then next line
    # Found it! The loop reads the first line into data, 
    # but inside the while loop, 
    # you're assigning the next line to data1 instead of data.
    #  Since data never changes, data != "" is always true—causing an infinite loop.


f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))  #type of data which is string
f.close()

f = open("demo.txt", "rt")
data = f.read()
print(data)
print(type(data))  #r and rt are same because text is default
f.close()

f = open("demo.txt", "rb")
data = f.read()
print(data)   #binary file readind
print(type(data))
f.close()

f = open("demo.txt", "r")
data = f.read(6)
print(data)    #only 6 characters printed
print(type(data))
f.close()

# reads single line
f = open("demo.txt", "r")
data = f.readline()
print(data)     #if there is next line present only then it will
f.close()       # print new blank line

# hi i am learning python

# blank line also

# append file
f=open("demo.txt","a")
f.write("this is a new python.\n")

# write file
f=open("demo.txt","w")
f.write("this \n")

# r+ 
# r+ overwrites the string from starting of file
f=open("demo.txt","r+")
f.write("this is amazing123")
f.close()
# r+ will have a little bit problem in overwriting especially in newline 1,2,3,4
# or

f=open("demo.txt","r+")
f.write("this is amazing")
print(f.read())
f.close()
# this is amazingzing for real
# zing for real  read function
# because pointer after writing is now at g so, zing for real  is printed

# w+
f=open("demo.txt","w+")
print(f.read())
f.write("this is amazing")
f.close()    #nothing will be printed
# because write will first truncate all the file
# then at last demo.txt will have this is amazing

f=open("demo.txt","w+")
f.write("this is amazing11")
print(f.read())
f.close()   
# print nothing because pointer is at 1 so nothing left to read
#  a+
f = open("demo.txt", "a+")
print(f.read())
f.write("234")
f.close()
# or
f=open("demo.txt","a+")
f.write("234")
print(f.read())
f.close()
# at start abc was there in demo.txt
# both will have same output
# demo.txt wil have 234 added at the end of demo.txt file
# op will be  abc234
# pointer will be at end of demo file

# with syntax
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)  #prints data in demo.txt

with open("demo.txt", "w") as f:
    f.write("new data")
# delete everything and write new data


# deleting a file

import os
os.remove("demo.txt")

# Create a new file “practice.txt” using python. Add the following data in it: 
# Hi everyone
# we are learning File I/O
# using Java. 
# I like programming in Java.

f=open("practice.txt","w")
f.write("""Hi everyone
we are learning File I/O
using Java. 
I like programming in Java.""")

# WAF that replace all occurrences of “java” with “python” in above file.
f=open("practice.txt","r")
data=f.read()
newdata=data.replace("Java","Python")
print(newdata)

f=open("practice.txt","w")
f.write(newdata)

# below cant be used
f=open("practice.txt","r+")
data=f.read()
newdata=data.replace("Java","Python")
print(newdata)
f.write(newdata)  
# pointer movement after reading is at end




#  QUESTION:
#  Search if the word “learning” exists in the file or not. 

f = open("practice.txt", "r")
data = f.read()
newdata = data.find("learning")
print(newdata)
if newdata < 0:   #or if "learning" in data
    print("not found")
else:
    print("found")

# if it is not found find function gives -1 
# so 0 is used in if statement


# or


f = open("practice.txt", "r")
data = f.read()
if "learning" in data:   
    print("found")
else:
    print(" not found")
##############

f = open("practice.txt", "r")
data = f.read()
newdata = data.find("learning")
print(newdata)
# returns index where it is found 
# or

# 
f=open("practice.txt","r")
data=True
line=1
while data:
    data=f.readline()
    if(data.find("learning")):
        print(line)
    else:
        line+=1
# find() gives index so if it is at 0th index 
# statement becomes false so thatswhy


# check in which line does the word exists
f=open("practice.txt","r")
data=True
line=1
while data:
    data=f.readline()
    if("learning" in data):
        print(line)
    else:
        line+=1

# inside a function

def func():
    f = open("practice.txt", "r")
    data = True
    line = 1
    while data:
            data = f.readline()
            if "learning" in data:
                print(line)
                return
            line += 1
    return -1      
# if word not present nothing will print  
func()

# From a file containing numbers separated by comma, print the count of even numbers.


with open("practice.txt","r") as f:
    data=f.read()
    print(len(data))
    num=""
    for i in range(len(data)):
        if(data[i]==","):
            print(num)
            num=""
        else:
            num= num+data[i]    #5 is s string and 6 is a string also
                                #so to get whole number we use + symbol whih is used to join 2 strings 
                                # string concatenation 
                                #  data[i] is the single character



with open("practice.txt","r") as f:
    data=f.read()
    print(len(data))
    num=""
    for i in range(len(data)):
        if(data[i]==","):
            print(int(num))
            num=""
        else:
            num= num+data[i]    


with open("practice.txt", "r") as f:
    data = f.read()
    print(len(data))
    num = ""
    for i in range(len(data)):
        if data[i] == ",":
            if int(num) % 2 == 0: 
                print(int(num))
            num = ""
        else:
            num = num + data[i]

# or

f = open("practice.txt", "r")
data = f.read()
newdata=data.split(",")
print(newdata)
count=0
for i in newdata:
    if(int(i)%2==0):
        count+=1
    else:
        pass

print(count)

# or
f = open("practice.txt", "r")
data = f.read()
num = ""
count=0
for i in range(0, len(data)):
    if data[i] == ",":
        print(int(num))
        if (int(num)%2==0):
            count=count+1
        num = ""
    else:
        num = num + data[i]
print(count)