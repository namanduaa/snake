
class student:
    name="naman"
    def hello(self):
        print("hello",self.name)

s1=student()
# print(s1.name)
s1.hello()
##############################3
class student:
    number=44
    def __init__(self):
        pass
print(student.number)

############################
# del keyword 
# to delete the object or object attribute like name, etc.
class student:
    def __init__(self,name):
        self.name=name
        print(name)

s1=student("naman")
del s1.name
print(s1.name)
# Class attribute = a property common to all (e.g., all cars have 4 wheels).
# Object attribute = a property unique to each (e.g., color or brand of a specific car).

###########################

class student:
    def hello(self):
        print("hello world")
    def welcome(self):
        self.hello()

# Why nothing printed before:

# You defined the class but never instantiated it
# You never called any methods
# Classes are just blueprints - 
# they don't execute until you create an object and use it
########################################################

class student:
    @staticmethod
    def hello():
        print("hello world")
    @staticmethod
    def welcome():
        student.hello()

s1=student()
s1.welcome()
# The issue: When you write just hello(), 
# Python looks for a function called hello in the global scope,
# but it doesn't exist. Since hello is a static method inside the student class, 
# you must call it using student.hello().

##############################################
# public attribute &method
class student:
    def __init__(self,name):
        self.name=name

s1=student("naman")
print(s1.name)      #example of public attribite(name variable accessed from outside of scope of class)

#####################################
class account:
    def __init__(self,name,password):
        self.name=name
        self.__password=password

user1=account("naman",12345)
print(user1.name)
print(user1.__password)

# example of private attribute means private variable (password)
# put 2 underscore in front of variable it will become private variable

class student:
    __name="naman"

s1=student()
print(s1.__name)
###################################################
class student:
    name="naman"
    def __hello(self):
        print("hello")  # private method

s1=student()
# print(s1.name)
s1.__hello()
###################################################
class student:
    def __hello(self):
        print("hello world")
    def welcome(self):
        self.__hello()

s1=student()
s1.welcome()        #private attr is used when ther is internal calling in the class
##########################################333
class car:
    color="blue"
    seats=4

class toyota(car):
    pass

car1=car()
print(toyota.color)     #color will be blue
##########################################3
class car:
    color = "blue"
    seats = 4

class toyota:
    seats = 7

s1 = toyota()
print(s1.seats)

s1 = car()
print(s1.seats)
#########################################
# inheritance 
class car:
    @staticmethod
    def start():
        print("car started.")
    @staticmethod
    def stop():
        print("car stopped.")
class toyota(car):
    def __init__(self):
        self.start()

s1 = toyota()
# print(s1.seats)
########################
class car:
    @staticmethod
    def start():
        print("car started.")
    @staticmethod
    def stop():
        print("car stopped.")

class toyota(car):
    def __init__(self,name):
        self.name=name
        self.start()

s1 = toyota("fortunar")     #prints car started
s2= toyota("camry")         #prints car started
# toyota gets called 2 times 
#########################################################
class car:
    @staticmethod
    def start():
        print("car started.")

    @staticmethod
    def stop():
        print("car stopped.")


class toyota(car):
    def __init__(self, name):
        self.name = name


s1 = toyota("fortunar")  # prints car started
s2 = toyota("camry")  # prints car started
# toyota gets called 2 times
print(s1.name)
s1.start()
###################################################
class car:
    @staticmethod
    def start():
        print("car started.")
    @staticmethod
    def stop():
        print("car stopped.")
class toyota(car):
    def __init__(self,brand):
        self.brand=brand

carr=toyota("ffff")
print(carr.brand)

class fortunar(toyota):
    def __init__(self, type):
        self.type=type

car1=fortunar("diesel")
print(car1.type)
car1.start()
print(car1.brand)
        
# Bottom line: Attributes ARE inherited, 
# but you must call the parent's __init__ 
# using super() to properly initialize them.

# When you created cc = model("2022"), 
# the model instance never initialized self.name 
# because toyota's __init__ was never called. 
# The name attribute exists in the toyota class, 
# but it wasn't set up for the model instance.
########################################################
class car:
    @staticmethod
    def start():
        print("car started.")
    @staticmethod
    def stop():
        print("car stopped.")
class toyota(car):
    def __init__(self,brand):
        self.brand=brand

class fortunar(toyota):
    def __init__(self, type):
        self.type=type

car1=fortunar("diesel")
print(car1.type)
car1.start()
####################################
class A:
    varA="this is a variable A."
class B:
    varB="this is a variable B."

class C(A,B):
    varC="this is a variable C."

VARIABLE=C()
print(VARIABLE.varC)
print(VARIABLE.varB)
print(VARIABLE.varA)
######################################
class car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car started.")
    @staticmethod
    def stop():
        print("car stopped.")

carr=car("fortunar")

class toyota(car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)          # self.type=type      this will also works the same        #nam nam ka super hai
        super().start()
car1=toyota("camry","fortunar")         #type is fortunar       whatever is written here will be printed 
print(car1.type)
#############################3
