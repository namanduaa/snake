class student:
    name="karan"

s1=student()
print(s1.name)
####################
class student:
    def __init__(self):  # default constructor
        pass
    def __init__(self,fullname): # parameterized constructor
        self.name=fullname

s1=student("naman")
print(s1.name)

#####################

class student:
    def __init__(self,fullname): # constructor having self and fullname as parameter 
        self.name=fullname    #self is the reference of object s1 in this case 
                              # so self.name is s1.name 
s1=student("naman dua")         #fullname is "karan"
print(s1.name)
#####################
class student:
    def __init__(self,fullname,number):
        self.name=fullname
        self.marks=number

s1=student("naman dua",99)
print(s1.name)
print(s1.marks)
###########################
class student:
    def __init__(self,fullname,number):
        self.name=fullname
        self.marks=number

s1=student("naman dua",99)
print(s1.name)
print(s1.marks)

s2=student("karan",99)

print(s2.name)
print(s2.marks)
#####################

class student:
    def __init__(self,fullname,number,college):
        self.name=fullname
        self.marks=number
        self.college=college

s1=student("naman dua",99,"mastnath")  #this causes increase in code redundancy 
print(s1.name)      
print(s1.marks)
print(s1.college)
s2=student("karan",99,"mastnath")       #mastnath is being written againand again so we use other thing
print(s2.name)                          #see next code 
print(s2.marks)
print(s2.college)

#  better option

class student:
    college="mastnath"
    def __init__(self,fullname,number):
        self.name=fullname
        self.marks=number
        # self.college=college   # no need to write this 

s1=student("naman dua",99)     #no need to write mastnath here againa and again for different students
print(s1.name)
print(s1.marks)
print(s1.college)
s2=student("karan",99)
print(s2.name)
print(s2.marks)
print(s2.college)
####################################

class student:
    college="mastnath"
    name="unknown"
    def __init__(self,fullname,number):
        self.name=fullname
        self.marks=number       


s1=student("naman dua",99)     
print(s1.name)          # object attribute > class attr  
print(s1.marks)         #so s1.name will print "naman dua" instead of "unknown"
print(s1.college)
s2=student("karan",99)
print(s2.name)          #same for this 
print(s2.marks)
print(s2.college)
###########################################

class student:
    college="BMU"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def welcome(self):                  #functions in classes are called methods 
        print("your welcome,",self.name)

    def get_marks(self):
        return self.marks


s1=student("naman", 78 )
print(s1.name)      #naman
print(s1.marks)     #78
print(s1.get_marks())   # function  in the class is called of s1 so,  78 will be printed because of (s1)


s2=student("karan",77)
print(s2.get_marks())   #same for this s2 has 77 marks

s1.welcome()    #welcome function is called  your welcome,naman  will be printed 

s2.welcome()    #welcome function is called  your welcome,karan  will be printed 

#######################################################################################3

class car:
    size = "hatchback"

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def life(self):
        print("lide of this car is ", self.width)

    def seats(self):
        print("you car is,", self.length)


suzuki = car("20m", 15)
honda = car("8m", 7)
tata = car("40m", 35)

print(suzuki.length)
print(suzuki.width)
print(suzuki.size)
suzuki.life()
suzuki.seats()  # object name.function name suzuki.seats

print(tata.length)
print(tata.width)
print(tata.size)
tata.life()
tata.seats()  # same here tata.seats

print(honda.length)
print(honda.width)
print(honda.size)
honda.seats()  # honda.seats
honda.life()
#############################3######
class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        avg = 0
        for i in self.marks:     # marks is a variable 
            avg += i        # every i contains value from marks
        return avg/3


list = [88, 99, 97]
s1 = student("naman", list) 
print(s1.average())
##################################################

# decorator or static method

class student:

    @staticmethod
    def hello():                #working of function without self 
        print("hello world ")

s1=student()
s1.hello()

##############################################33
class car:
    def __init__(self):
        self.race=False
        self.brake=False
        self.clutch=False   
        print(self.clutch)  # this doennot work until object is made 
                            # because constructor is not activated until object is made
    def start(self):
        self.race=True
        self.clutch=True        #both race are same one variable 
        print(self.race)

car1=car()       #related to this line where object is created
car1.start()     # Both references use self, which always points to the current object instance, 
                 #so they're updating the same variable in the car1 object.

################################333

# abstraction 

class car:
    def __init__(self):
        self.race=False
        self.brake=False
        self.clutch=False   

    def start(self):
        self.race=True              #abstraction example 
        self.clutch=True            #other details regarding race barake are hiden from user 
        print("car started")

car1=car()                  
car1.start()                        #car gets started user satisfied

###################################3

class Car:
    def __init__(self):
        self._speed = 0  # Private variable (convention: single underscore)
        self._fuel = 100
    
    def accelerate(self):
        """Public method to safely increase speed"""
        if self._fuel > 0:
            self._speed += 10
            self._fuel -= 5
            print(f"Speed: {self._speed}, Fuel: {self._fuel}")
        else:
            print("No fuel!")
    
    def get_speed(self):
        """Getter method - control how speed is accessed"""
        return self._speed
    
    def set_speed(self, speed):
        """Setter method - control how speed is modified"""
        if speed < 0:
            print("Speed cannot be negative!")
        else:
            self._speed = speed
            print(self._speed)

# Usage
car1 = Car()
car1.accelerate()      # Speed: 10, Fuel: 95
car1.accelerate()      # Speed: 20, Fuel: 90

# Can only access/modify through controlled methods
print(car1.get_speed())  # 20
car1.set_speed(-5)       # Speed cannot be negative!
car1.set_speed(50)       # Valid

#_speed, _fuel	 ->     Data	Store information
# accelerate()   ->	Function	Performs an action (increases speed, uses fuel)
# get_speed()	 ->  Function	Returns/retrieves data
# set_speed()	 ->   Function	Modifies data with validation

# The class is a template that defines what data and functions should exist.
# Each object is a real instance with its own data and can use the functions.

# In simple terms:

# Class = Contains the structure/definition of data and functions
# Object = An actual working instance where data has real values and functions can be executed
# So to answer directly: Both are encapsulated in the CLASS, but they operate in the OBJECT.


# CLASS                          OBJECTS
# ┌─────────────────┐        ┌──────────┐    ┌──────────┐
# │  Car (Template) │        │  car1    │    │  car2    │
# ├─────────────────┤        ├──────────┤    ├──────────┤
# │ _speed = 0      │ ────→  │ _speed=0 │    │ _speed=50│
# │ _fuel = 100     │        │ _fuel=95 │    │ _fuel=80 │
# │ accelerate()    │        │ methods  │    │ methods  │
# │ get_speed()     │        └──────────┘    └──────────┘
# └─────────────────┘


#############################################################33
# practical experience of updating ,credit,debit of an account

class account:
    def __init__(self,balance,accno):
        self.balance=balance
        self.accno=accno

    def debit(self,amount):
        self.balance-=amount
        print(f"Rs. {amount} was debited and updated balance is {self.balance}")
       

    def credit(self,amount):
        self.balance+=amount
        print(f"Rs.{amount} was credited and updated balance is {self.balance} ")
    def balanceprint(self):
        print(f"total balance of your account is {self.balance}")

user1=account(1000,79885)

user1.debit(300)
user1.credit(500)
user1.balanceprint()

# or 

class account:
    def __init__(self,balance,accno):
        self.balance=balance
        self.accno=accno

    def debit(self,amount):
        self.balance-=amount
        print(f"Rs. {amount} was debited and updated balance is {self.balance}")
       

    def credit(self,amount):
        self.balance+=amount
        print(f"Rs.{amount} was credited and updated balance is {self.balance} ")
    def balanceprint(self):
        print(f"total balance of your account is {self.balance}")

user1=account(1000,79885)

user1.debit(300)
user1.credit(500)
user1.balanceprint()
user1.debit(500000)
user1.credit(1000000)