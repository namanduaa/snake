
# Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50        
# => F 
a = int(input("enter the name"))
if a <= 100 and a >= 90:
    print("EX")
elif a <= 100 and a >= 90:
    print("EX")
elif a < 90 and a >= 80:
    print("A")
elif a < 80 and a >= 70:
    print("B")
elif a < 70 and a >= 60:
    print("C")
elif a < 60 and a >= 50:
    print("D")
elif a < 50:
    print("fail")

# Write a program to find out whether a given post is talking about “Naman” or not.
post=input("enter the post: ")
if("Naman".lower() in post.lower()):
    print("yes")
else:
    print("no")
# lower conver th post and Naman in lower case and checks after that post ids talking about Naman or not

# Write a program to print multiplication table of a given number using for loop. 
n = int (input("enter the number: "))
for i in range(1,11):
    print(i*n)
# OR
n = int(input("enter the number: "))
for i in range(1,11):
    print(f"{n}*{i}={n*i}") 

# Write a program to greet all the person names stored in a list ‘l’ and which starts 
# with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]
for i in l:
    if(i.startswith("S")):
        print(f"you are welcome,{i}")

 
# Attempt problem 1 using while loop. 
n = int(input("enter the number"))
i=1
while(i<11):
    print(f"{n}*{i}={n*i}")
    i+=1

# Write a program to find whether a given number is prime or not. 
n = int(input("enter the number :"))
for i in range(2, n):
    if n % i == 0:
        print(f"{n} is not a prime number.")
        break
    else:
        print(f"{n} is a prime number.")
        break

# Write a program to find the sum of first n natural numbers using while loop. 
n = int(input("enter the number :"))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i = i + 1
    
print(f"sum of first {n} natural no. is :", sum)
# OR
n = int(input("enter the number :"))
sum = 0
for i in range(1,n+1):
    sum +=i
print(sum)

# Write a program to calculate the factors of a given number using for loop. 

n = int(input("enter the number :"))
integer= not float
for i in range(1,n+1):
    if(n%i == integer):
        print(i)
# Write a program to calculate the factorial of a given number using for loop.
n = int(input("enter the number :"))
final=1
for i in range(1, n+1):
    final = final *i
print(final)

# Write a program to print the following star pattern. 
#   * 
#  *** 
# ***** for n = 3 

n = int(input("enter the number :"))
for i in range(1, n + 1):
    spaces = n - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)

# Write a program to print the following star pattern: 
# * 
# ** 
# ***      for n = 3 
n = int(input("enter the number :"))
for i in range(0, n ):
    stars = i + 1
    print("*" * stars)

# Write a program to print the following star pattern. 
# * * * 
# *   *   for n = 3 
# * * *  
# end="" means add nothing at the end (no newline)
# So all outputs stay on the same line
n = int(input("enter the number :"))
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * n)
    else:
        print("*", end="")
        print(" " * (n - 2), end="")
        print("*", end="")
        print() #next line
        
# OR
n = int(input("enter the number :"))
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")  

# Write a program to print multiplication table of n using for loops in reversed 
# order. 
n = int(input("enter the number :"))
for i in range(1,11):
    print(n*(11-i))

# pyton function to write greatest of 3 number
def great(a, b, c):
    if a > b and a > c:
        print(f"{a} is greatest")
    elif b > a and b > c:
        print(f"{b} is greatest")
    else:
        print(f"{c} is greatest")

great(33,24,3)

# convert celcius to fahrenhiet
def convert(celcius):
    fahrenhiet = ((9 / 5 )* celcius)+32
    return fahrenhiet

print(convert(20))    

# prevent python print() function to print new line
print("a",end="") ;print("b",end="")

# write sum of first n natural numbers
def sum(n):
    if n == 1:
        return 1
    return sum(n - 1) + n
print(sum(7))

# Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# *   for n = 3

i=3
def reverse(i):
        i = 3
while i > 0:
        print("*" * i)
        i = i - 1

reverse(3)
# or
def reverse(i):
    while i > 0:
        print("*" * i)
        i = i - 1

reverse(4)
# or
stars="*"
i=4
while(i>0):
    print(stars*i)
    i=i-1

# or
def stars(n):
    if n == 0:
        return
    print("*" * n)
    stars(n - 1)

stars(5)

# Write a python function which converts inches to cms. 
def convert(inches):
    cm = 2.54 * inches
    print(f"{inches} inches ={cm} cm")
    return cm

print(convert(6))

# Write a python function to remove a given word from a list ad strip it at the same 
# time. 
list1 = ["ab", "fuck", 55, False, 77.44]

def remove(list1):
    list1.remove("ab")
    return list1

print(remove(list1))
# or
l = ["naman", "aman", "shubham", "an", "rahul"]
word=input()

def rem(l, word):
    for item in l:
        l.remove(word)
        return l


print(rem(l,word))
# or
l = ["aman", "shubham", "an", "rahul"]

def rem(l, word):
    n=[]
    for item in l:
        if not(item ==word):
            n.append(item.strip(word))
    return n

print(rem(l,"an"))

# Write a python function to print multiplication table of a given number.
n = int(input("enter the number:"))

def table(n):
    i = 1
    while i < 11:
        print(n * i)
        i = i + 1

table(n)



countries=["America","Canada","Australia","China","Chile"]
for c in countries[:]:
    if c.startswith("C"):
        countries.remove(c)
print(countries)        