# Store following word meanings in a python dictionary : 
# table : “a piece of furniture”, “list of facts & figures”
# cat : “a small animal”

dict={
    "table":["a piece of furniture","list of facts & figure"],
    "cat":" a small animal"
}
print(dict)

# You are given a list of subjects for students. Assume one classroom is required for 1
# subject. How many classrooms are needed by all students.
# ”python”, “java”, “C++”, “python”, “javascript”,
# “java”, “python”, “java”, “C++”, “C”

# we will use set because it will npt count the duplicate elements
set={"python","java","javascript","c","c++"}
print(len(set))  #5


# WAP to enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary & add one by one. Use subject name as key & marks as value


dict={}
physics=int(input("enter the number:"))
chemistry=int(input("enter the number:"))
maths=int(input("enter the number:"))
dict.update({"physics":physics})
dict.update({"chemistry":chemistry})
dict.update({"maths":maths})
print(dict)
print(type(dict))

# Figure out a way to store 9 & 9.0 as separate values in the set. 
# (You can take help of built-in data types) 

set = {(9,9,0)}
print(set) # AS A TUPLE and then save it

set = {9, "9.0"}
print(set) # as a int and as a float


# Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up!

dict = {       
        "pani": "water",
        "seb": "apple",
        "madad":"help",
        "khana":"food",
         }
print(dict)
word = input("enter the word to look it up:")
print(dict.get(word))

# Write a program to input eight numbers from the user and display all the unique 
# numbers (once). 
a=int(input("enter the number= "))
b=int(input("enter the number= "))
c=int(input("enter the number= "))
d=int(input("enter the number= "))
e=int(input("enter the number= "))
f=int(input("enter the number= "))
g=int(input("enter the number= "))
h=int(input("enter the number= "))

set={a,b,c,d,e,f,g,h}
print(set)

# OR

set=set()
a=int(input("enter the number= "))
set.add(a)
a=int(input("enter the number= "))
set.add(a)
a=int(input("enter the number= "))
set.add(a)
a=int(input("enter the number= "))
set.add(a)
a=int(input("enter the number= "))
set.add(a)
a=int(input("enter the number= "))
set.add(a)
a=int(input("enter the number= "))
set.add(a)
a=int(input("enter the number= "))
set.add(a)

print(set)

# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.


dict={}
aman=input("enter the favourite subject:")
naman=input("enter the favourite subject:")
rahul=input("enter the favourite subject:")
kartik=input("enter the favourite subject:")
dict.update({"aman":aman,"naman":naman,"rahul":rahul,"kartik":kartik})
print(dict)

# OR 

dict={}
name=input("enter the name=")
lang=input("enter the language")
dict.update({name:lang})
name=input("enter the name=")
lang=input("enter the language")
dict.update({name:lang})
name=input("enter the name=")
lang=input("enter the language")
dict.update({name:lang})
name=input("enter the name=")
lang=input("enter the language")
dict.update({name:lang})

print(dict)


#  If the names of 2 friends are same; what will happen to the program in problem 
# 6? 

dict={}
name=input("enter the name=")
lang=input("enter the language")
dict.update({name:lang})
name1=input("enter the name=")
lang1=input("enter the language")
dict.update({name1:lang1})
name2=input("enter the name=")
lang2=input("enter the language=")
dict.update({name2:lang2})
name3=input("enter the name=")
lang3=input("enter the language=")
dict.update({name3:lang3})

print(dict)

# {'naman': 'pp', 'aman': 'c++', 'kaka': 'js'}
# key's value  gets updated,

# If languages of two friends are same; what will happen to the program in problem 
# 6?

# {'naman': 'pp', 'aman': 'cc', 'rohan': 'cc'}
# values can be same of different keys

#  Write a program to find the greatest of four numbers entered by the user.

a1=int(input("enter the number= "))
a2=int(input("enter the number= "))
a3=int(input("enter the number= "))
a4=int(input("enter the number= "))

if(a1>a2 and a1>a3 and a1>a4):
    print(f" a1 is greatest.",{a1})

elif(a2>a3 and a2>a3 and a2>a4):
    print(" a2 is greatest.",a2)

elif(a3>a2 and a3>a1 and a3>a4):
    print(" a3 is greatest.",a3)

else:
    print(" a4 is greatest.",a4)

# OR

a=int(input("enter the number:(0-100)="))
b=int(input("enter the number:(0-100)="))
c=int(input("enter the number:(0-100)="))
print(max(a,b,c))

# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 

phy=int(input("enter the number:(0-100)="))
chem=int(input("enter the number:(0-100)="))
bio=int(input("enter the number:(0-100)="))
total=((phy + chem + bio)/300)*100
if(phy >=33 and chem>=33 and bio>=33 and total >=40):
    print("pass")
else:
    print("fail")

# A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams. 

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

a=input("enter the string :")
if((p1 in a)or(p2 in a)or(p3 in a)or(p4 in a)):
    print("spam")
else:
    print("no spam")

# Write a program to find whether a given username contains less than 10 
# characters or not. 


a=input("enter the name=")
if(len(a)<10):
    print("short name")
else:
    print("good name")

# Write a program which finds out whether a given name is present in a list or not. 
list=["naman","harry","kaka","sane","mane"]
a= input("enter the name")
if(a in list):
    print("yes")
else:
    print("no")
