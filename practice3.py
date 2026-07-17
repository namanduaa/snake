# Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’.

f=open("practice.txt","r")
data=f.read()
lowerdata=data.lower()
countdata=lowerdata.count("twinkle")
print(countdata)

# The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi
# score whenever the game() function breaks the Hi-score.
 
import random
def game():
    score=random.randint(1,60)
    print(f"your score is {score}")
    f=open("practice.txt","r")
    data=f.read()
    if (data!=""):
        number=int(data)
    else:
        number =0       # 0 here is a integer and starter if there is blank string 
    if(number =="" or score > number):
        f=open("practice.txt","w")
        f.write(str(score))     # str because everything in text file is string thats why

    return score

game()

# Write a program to generate multiplication tables from 2 to 20 and write it to the 
# different files. Place these files in a folder for a 13 – year old. 

def table(i):
    for j in range(1,11):
        f=open(f"practice{i}","a")
        table=i*j
        table1=(str(table))
        f.write(table1)
        f.write("\n")

for i in range(2,21):
    table(i)    #function calling in loop

# A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file.

f=open("practice.txt","r")
data=f.read()
newdata=data.replace("donkey","######")
f=open("practice.txt","w")
f.write(newdata)

# Repeat program 4 for a list of such words to be censored. 

list=["donkey","bad","ganda"]

with open("practice.txt","r") as f:
    data=f.read()
    for i in list:   #firstly donkey will bw replaced then bad in a loop
        data=data.replace(i,"#"*len(i))

with open("practice.txt","w") as f:
    f.write(data)
# Write a program to mine a log file and find out whether it contains ‘python’. 

with open("practice.txt","r") as f:
    data = f.read()
    if "python" in data:
        print("found")
    else:
        print("not found")
# Write a program to mine a log file and find out whether it contains ‘python’. 


# Write a program to find out the line number where python is present from ques 6. 

with open("practice.txt","r")   as f:
    data =True
    line=1
    while data:
        data=f.readline()
        if ("python" in data):
            print(line)
            line+=1
        else:
            line+=1
# Write a program to find out the line number where python is present from ques 6.

with open("practice.txt","r") as f:
    data=f.readlines()
    line=1
    for i in data:
        if("python" in i):
            print(line)
            line+=1
        else:
            line+=1
# Write a program to make a copy of a text file “this. txt” 

with open("practice.txt","r") as f:
    data=f.read()
with open("this.txt","w") as f:
    f.write(data)
# Write a program to find out whether a file is identical & matches the content of 
# another file. 

with open("practice.txt", "r") as f:
    data = f.read()
with open("this.txt", "r") as f1:
    data1 = f1.read()

if data == data1:
    print("match found")
else:
    print("not the same")

# Write a program to wipe out the content of a file using python. 
f=open("this.txt","w")
#  Write a python program to rename a file to “renamed_by_ python.txt. 
import os
with open("practice.txt","r") as f:
    data=f.read()
with open ("rename_by_python","w") as f:
    f.write(data)

os.remove("practice.txt")