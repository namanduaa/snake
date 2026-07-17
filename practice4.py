# define circle class to create a circle with radius r.Define an Area() method which calculate the area of circle
# Define a perimeter() method of the class which allows you to calculate perimeter of circle.
class circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

    def peri(self):
        return 2 * 3.14 * self.r


radius = circle(5)
print(radius.area())
print(radius.peri())


#


# define a employee class with attribute role,department and salary.This class also has a showDetails() method.
# Create an Engineer class that inherits properties from employee and has additional attributes:name & age.


class employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showdetails(self):
        print(f"role={self.role}")
        print(f"department={self.department}")
        print(f"salary={self.salary}")


class engineer(employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("technical", "IT", 75000)

    def showdetail(self):
        print(f"name={self.name}")
        print(f"age={self.age}")


engg1 = engineer("naman", 21)
engg1.showdetails()
engg1.showdetail()


#

# create a class called order which stores items and its price
# use dunder function __gt__() to convey that,
# order1>order2 if the price of order1> order2


class order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return (
            self.price > order2.price
        )  # magic of dunder function  related by > operator
        # > is used here for price


order1 = order("banana", 60)
order2 = order("mango", 50)

print(
    order1 > order2
)  # True   > is used here of gt function  thats why true or false is printed by referncing > operator

# Why this matters:

# Normally, > only works with numbers/strings
# By defining __gt__, you teach the > operator how to compare custom objects
# So order1 > order2 automatically becomes order1.price > order2.price


#


# Write a class “Calculator” capable of finding square, cube and square root of a
# number.
class calculator:
    def square(self, n):
        return n * n

    def cube(self, n):
        return n * n * n

    def root(self, n):
        return n ** (1 / 2)


number = calculator()
print(number.square(5))
print(number.cube(5))
print(number.root(64))


#

# Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?


class demo:
    a = 4


obj = demo()
print(obj.a)        # prints the class attribute because because instance attribute is not present
obj.a = 0           #instance attribute is set
print(obj.a)  # 0   prints the instance attribute

print(demo.a)  # 4  prints the class attribute


#


# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.


import random  #from random import randint

class train:
    def __init__(self, fro, to):
        self.fro = fro
        self.to = to

    def book(self):
        print(f"your train is booked from {self.fro}  to {self.to}")

    def fare(self):
        print(f"your fare is {random.randint(222,555)}")            #her randint will work also if from is used in import

    def getstatus(self):
        print("your train is on time ")

train1 = train("delhi","jaipur")
train1.book()
train1.fare()
train1.getstatus()


# 


# Can you change the slf-parameter inside a class to something else (say
# “harry”). Try changing slf to “slf” or “harry” and see the effects.

import random

class train:
    def __init__(slf, fro, to):
        slf.fro = fro
        slf.to = to

    def book(slf):
        print(f"your train is booked from {slf.fro}  to {slf.to}")

    def fare(slf):
        print(f"your fare is {random.randint(222,555)}")

    def getstatus(slf):
        print("your train is on time ")

train1 = train("delhi","jaipur")
train1.book()
train1.fare()
train1.getstatus()


