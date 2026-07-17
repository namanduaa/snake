for i in range(1,6):
    print(i)

l =[2,4,6]
for i in l:
    print(i)
# OR
l =[2,4,6]
for i in range(0,len(l)):
    print(l[i])


i=1
while(i<6):
    print(i)
    i=i+1

#  Write a program to print the content of a list using while loops.

list=[33,44,"naman",False,"aman",77.88]
i=0
while(i<len(list)):
    print(list[i])
    i+=1

# OR
list=[33,44,"naman",False,"aman",77.88]
for i in range(0,len(list)):
    print(list[i])

# OR

list=[33,44,"naman",False,"aman",77.88]
for i in list:
    print(i)

# use of range function with the gap of 4
for i in range(0,101,4):
    print(i)

a= "namand"
for i in a: #this line decides how many times the loop runs which is 6 in this case ,because there are 6 characters in a string
    print(a) #naman will be printed 6 times  loop material will be printed 6 times


# Line 1: a = "naman"

# Creates a string variable a with value "naman"
# Strings are sequences of characters
# Line 2: for i in a:

# This is a for loop that iterates (goes through) each character in the string a
# The loop runs 5 times because "naman" has 5 characters
# Each iteration, the variable i gets assigned the current character:
# Iteration 1: i = 'n'
# Iteration 2: i = 'a'
# Iteration 3: i = 'm'
# Iteration 4: i = 'a'
# Iteration 5: i = 'n'
# Line 3: print(a)

# Prints the entire string a (which is always "naman")
# This runs 5 times because the loop runs 5 times
# The variable i is never used in the print statement

a="naman"
for i in a:
    print(i)


l= [1,7,8] 
for item in l: 
    print(item) 
else: 
    print("done") 

list=[33,44,"naman",False,"aman",77.88]
for i in list:
    if(i == False):
        break
    print(i)

for i in range(26):
    if(i==15):
        break
    print(i)

for i in range(26):
    if(i==15):
        continue
    print(i)

for i in range(26):
    if(i==15):     # 15
        break
print(i)

for i in range(26):
    if(i==15):
        continue
print(i)

for i in range(26):
    if(i==15):
        pass
print(i)

for i in range(0, 10):
    pass

print(i)   # use of pass statement makes sures 
i = 0      # it skip for loop and focus on other loop in this case
while i < 10: #pass means do nothing 
    print(i)
    i += 1
