# polymorphism
# when one operator is used my many and have different results according to input
# like plus operator
print(1 + 2)
print(type(1))  # here plus adds 2 number
print("apna" + "college")
print(type("apna"))  # here plus concatenate strings
print([1, 2, 3] + [4, 5, 6])
print(type([1, 2, 3]))  # here plus merges 2 lists

# 

class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def number(self):
        print(f"{self.real}i+ {self.img}j")

num1=complex(1,3)
num2=complex(2,5)
num1.number()
num2.number()


# 


class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def number(self):
        print(f"{self.real}i+ {self.img}j")

    def add(self, num2):
        newReal = self.real + num2.real
        newimg = self.img + num2.img
        return complex(newReal, newimg)

num1 = complex(1, 3)
num1.number()

num2 = complex(2, 5)
num2.number()

num3 = num1.add(num2)  # num3=complex(3,8)  num1 is self and add(num2) is function calling ,num2 is (2,5)
num3.number()           #num1 serves as self in these types of cases


# 
# we changed the meaning of minus in this case, this is what called operator overoading,use case of polymorphism
# dunder funnction
class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def number(self):
        print(f"{self.real}i+ {self.img}j")

    def __add__(self, num2):                #dunder function add is used 
        newReal = self.real + num2.real
        newimg = self.img + num2.img
        return complex(newReal, newimg)

num1 = complex(1, 3)
num1.number()

num2 = complex(2, 5)
num2.number()                                   

num3 = num1+num2                               # so now we can simply write num1 + num2 
num3.number()                                  # instead of num3=num1.add(num2)     ,num1 serves as self in these types of cases



# 

class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def number(self):
        print(f"{self.real}i+ {self.img}j")

    def __sub__(self, num2):                #dunder function add is used 
        newReal = self.real - num2.real
        newimg = self.img - num2.img
        return complex(newReal, newimg)

num1 = complex(4, 8)
num1.number()

num2 = complex(2, 5)
num2.number()

num3 = num1-num2                               # so now we can simply write num1 + num2 
num3.number()                                  # instead of num3=num1.add(num2)    , num1 serves as self in these types of cases



# 



class number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num5):
        return self.n + num5.n


num1 = number(2)
num2 = number(5)
print(num1 + num2)



# 


class number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num5):            # special method that Python calls for self + other
        return self.n + num5.n          #Parameter name num5 is just a variable name; it is expected to be another number instance
                                        

num1 = number(2)
num2 = number(5)
print(num1 + num2)          #print(num1 + num2) — calls num1.__add__(num2), returns 7, and prints 7.
                            # num1 is self and the num5 is num2means other in this case
                             # add is inbuilt so + operator calls __add__ function in this case and it returns 7 .




# 




