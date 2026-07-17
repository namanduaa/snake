a = 10
b = 20


def sum(x, y):
    print(x + y)


sum(a, b)

a = 10
b = 20


def sum(x, y):
    return x + y


print(sum(a, b))


def hello():
    print("hello world")


hello()


def hello():
    print("hello world")


print(hello())  # None


def average(a, b, c):
    average = a + b + c
    return average


print(average(30, 54, 66))
print(type(average(33, 54, 64)))  # type depends on the output


def average(a=1, b=2):
    average = a + b
    return average
    # default parameters when arguements are not passed in


print(average())  # 3


def average(a=1, b=2):
    average = a + b
    return average


print(average(6))  # 8
# because arguement is given preference over default parameter

# WAF to print the length of a list. ( list is the parameter)
list1 = [2, 44, False, True, 77.44, "naman"]
def length(list1):
    print(len(list1))
length(list1)

# WAF to print the elements of a list in a single line. ( list is the parameter)
list1 = [2, 44, False, True, 77.44, "naman"]
def oneline(list1):
    for i in range(0, len(list1)):
        print(list1[i], end=" ")
oneline(list1)
# OR OR
list1 = [2, 44, False, True, 77.44, "naman"]
def length(list1):
    for item in list1:
        print(item,end=" ")
length(list1)        

# WAF to find the factorial of n. (n is the parameter)
n = int(input("enter the number:"))
def factorial(n):
    final=1
    for i in range(1, n + 1):
        final = final * i
    print(final)
    
factorial(n)

# WAF to convert USD to INR.

n = int(input("enter the dollar:"))
def convert(n):
    usd = 90 * n
    print(usd)

convert(n)

# OR
n = int(input("enter the dollar:"))
def convert(n):
    usd = 90 * n
    print(f"{n} usd = {usd} inr")

convert(n)

# odd or even
n = int(input("enter the number:"))
def check(n):
    if(n%2==0):
        print("even")
    else:
        print("odd")

check(n)