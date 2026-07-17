str1="my name is "
str2="naman"
str3=str1+"   "+str2 #length of string and catenation
print(str3)
print(len(str3))


# ========================================================

str="naman dua"
ch = str[2]   #indexing in python
print(str[2])
print(ch)


# =============================================================

str="apna college"
print(str[:4]) #str[0:4] =apna
print(str[2:6]) #str[2:6] =na c
print(str[2:]) #str[2:len(str)] len because indexing is oth based =na college


# ================================================================================

str ="i am a very good coder."
str = str.capitalize()
print(str.capitalize())
print(str)

str ="i am a very good coder."
print(str.endswith("coder."))

str ="i am a very good coder."
print(str.replace("am","f"))

str ="i am a very good coder."
print(str.find("ov"))

str ="i am a very good coder."
print(str.count("o"))

a=int(input("enter the marks="))
if (a>=90):
    print("grade =A")
elif( a>=80 and a<90 ):
    print("grade =B")
elif(a>=70 and a<80):
    print("grade =C")
else:
    print("not good marks")

print("good luck")

a=8
if(a>=18):
    if(a>80):
        print("can not drive")
    else:
        print("candrive")
else:
    print("can not drive")

a=9
if(a%2==0):
    print("even")
else:
    print("odd")

#greatest of three
a= 8
b= 9
c= 10
print(max(a,b,c))

a=155
if(a%7==0):
    print("yes")
else:
    print("no")

a=int(input("enter a ="))
b=int(input("enter b ="))
c=int(input("enter c ="))
if(a>=b and a>=c):
    print("a is largest",a)
elif(b>=c):
    print("b is largest",b)
else:
    print("c is largest",c)

marks=[23,534,8.7,"naman"]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[1])


# ================================================================================================
# Is SSD the Same as ROM?
# No, but they both share one key trait: ✅ Non-volatile memory — they retain data even when the power is off.

# However, they serve different purposes:

# Feature	SSD (Solid State Drive)	ROM (Read-Only Memory)
# Function	General-purpose storage (OS, files, apps)	Stores firmware or boot instructions
# Size	Large (GB to TB)	Small (KB to MB)
# Writable?	Fully writable and erasable	Usually fixed or rarely updated
# Location	Installed as a drive	Embedded in motherboard or chip
# User Access	You can read/write freely	You can't modify directly (except Flash ROM)
# 🧠 So Why Do Phones Say “64GB ROM”?
# In phones, “ROM” is a misused term. It actually refers to the internal flash storage, which is technically an SSD-like chip. You can read, write, and delete files—so it’s not truly “read-only.”

# In laptops and PCs, we call this storage SSD or HDD, not ROM.

# ✅ Bottom Line:
# SSD is SSD—a fast, rewritable storage device.

# ROM is ROM—a small, fixed memory area for boot instructions.

# In phones, “ROM” = internal storage (but it’s really flash memory, like SSD).
# ==============================================================================
# Data Science & Machine Learning
# numpy – Numerical computing with arrays and matrices.
# pandas – Data manipulation and analysis.
# matplotlib – Data visualization and plotting.
# seaborn – Statistical data visualization.
# scikit-learn – Machine learning algorithms.
# tensorflow / torch – Deep learning frameworks.
''' My girlfriend dumped me after I named a class after her.
 She felt I treated her like an object.'''
"""============================="""
import os

# Specify the directory path (use '.' for current directory)
directory_path = "D:/"

try:
    # Get the list of all files and directories in the specified path
    contents = os.listdir(directory_path)

    print(f"Contents of directory '{directory_path}':")

    # Loop through the list and print each item
    for item in contents:
        print(item)

except FileNotFoundError:
    print("Error: The specified directory does not exist.")
except PermissionError:
    print("Error: You do not have permission to access this directory.")
"""============+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""