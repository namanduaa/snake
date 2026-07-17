# 1. Create a class (2-D vector) and use it to create another class representing a 3-D 
# vector. 


class twodvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"{self.i}i +{self.j}j")


class threedvector(twodvector):
    def __init__(self, i, j, k):
        self.k = k
        super().__init__(i, j)

    def show3d(self):
        print(f"{self.i}i +{self.j}j {self.k}k")


vector2 = twodvector(3, 4)
vector3 = threedvector(5,6,7)

vector2.show()
vector3.show3d()


# 



# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class animal:
    pass


class pets(animal):
    pass


class dog(pets):
    @staticmethod
    def bark():
        print("dog is barking")
        

dog1=dog()
dog1.bark()


# 


# Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
# which changes the value of increment based on the salary.


class employee:
    def __init__(self,salary,increment):
        self.salary=salary
        self.increment=increment
    @property
    def salaryafterincrement(self):
        print(f"salary after increment :{self.salary+self.increment}")

e1=employee(75000,25000)

e1.increment=70000
print(e1.salary)
print(e1.increment)
e1.salaryafterincrement


# 


class employee:
    salary = 75000
    increment = 25000

    @property
    def salaryafterincrement(self):
        print(f"salary after increment {self.salary+self.increment}")

    @salaryafterincrement.setter
    def salaryafterincrement(self, value):
        self.increment = value - self.salary


e1 = employee()
print(e1.salary)
e1.salaryafterincrement

#  changed manually                                                                                 #may be not goofd solution 
e1.salary = 90000
print("salary changed to", e1.salary)
e1.salaryafterincrement

# now changed manually
e1.salaryafterincrement = 120000
print(f"increment would be :{e1.increment}")
e1.salaryafterincrement



# 


# class employee:
#     salary=75000
#     increment=32.8
#     @property
#     def salaryafterincrement(self):
#         return (self.salary+ (self.salary*self.increment)/100)
#     @salaryafterincrement.setter
#     def salaryafterincrement(self,salary):
#         self.increment= ((salary/self.salary)-1)*100 

# e1=employee()

# print(e1.salaryafterincrement)

# print(e1.increment)


#



# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.


class complex:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def __add__(self, num2):
        ist=self.i+num2.i
        second=self.j+num2.j
        print(f"{ist}i+{second}j")
        

num1=complex(2,4)
num2=complex(6,8)

num1+num2


# 


# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.


class complex:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __add__(self, num2):
        ist = self.i + num2.i
        second = self.j + num2.j
        print(f"{ist}i+{second}j")

    def __mul__(self, other):
        real = self.i * other.i - self.j * other.j
        imag = self.i * other.j + self.j * other.i
        return complex(real, imag)

    def __str__(self):
        return f"{self.i} + {self.j}i"



num1 = complex(2, 4)
num2 = complex(6, 8)

num1 + num2
print(num1 * num2)



# 



# Write a class vector representing a vector of n dimensions. Overload the + and *
# operator which calculates the sum and the dot(.) product of them.


class vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, vector2):
        ist = self.i + vector2.i
        second = self.j + vector2.j
        third = self.k + vector2.k
        return vector(ist, second, third)

    def __mul__(self, vector2):
        dotproduct = self.i * vector2.i + self.j * vector2.j + self.k * vector2.k
        return dotproduct
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"


vector1 = vector(1, 2, 3)
vector2 = vector(4, 5, 6)

print(vector1 + vector2)
print(vector1 * vector2)
# When you pass that object to print(), 
# Python internally calls the __str__ method of the object to know how to represent it as a string.
# vector1 * vector2 calls your overloaded __mul__ method.

# That method returns a number (dot product), not a vector object.

# Since it’s just an integer, Python prints it directly without needing __str__.

# Key idea
# __str__ is automatically called whenever you try to print an object (or convert it to a string with str(obj)).

# If your method returns a primitive type (like int or float), Python doesn’t need __str__.

# If your method returns a custom object, Python looks for __str__ to decide how to display it.

# 👉 So in your code:

# vector1 + vector2 → returns a vector → print() calls __str__.

# vector1 * vector2 → returns an int → print() just shows the number.










# 



# 6. Write __str__() method to print the vector as follows:
# 7i + 8j +10k
# Assume vector of dimension 3 for this problem.

class vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"


vector1 = vector(7, 8, 10)
print(vector1)


# 



# Override the __len__() method on vector of problem 5 to display the dimension of the
# vector.


class vector:
    def __init__(self,l):
        self.l=l        # l has list in it
    def __len__(self):
        return len(self.l)      #it prints length of list

vector1 = vector([7, 8, 10,99])     #list is passed
print(len(vector1))