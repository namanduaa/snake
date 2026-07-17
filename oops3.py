class person:
    name = "anonymous"

    def __init__(self, name):  # here clas has a differnt name variable
        self.name = name


p1 = person("rahul")  # and a object self has differnt name variable
print(p1.name)  # so op will be rahul
print(person.name)  # anonymous


#######################################
class person:
    name = "anonymous"

    def __init__(self, name):
        person.name = name


p1 = person("rahul")
print(p1.name)  # so now changes will be in name variable of class
print(person.name)


################################
class person:
    name = "anonymous"

    def __init__(self, name):
        pass


p1 = person("rahul")
print(p1.name)
print(person.name)


################3333
class person:
    name = "anonymous"

    def __init__(self, name):
        self.__class__.name = name


p1 = person("rahul")
print(p1.name)
print(person.name)


######################
class person:
    name = "anonymous"  # we don't use constructor here because constructor name will take a name parametr

    @classmethod  # and student takes no arguemnt here ,error will be shown
    def changename(cls, name):
        cls.name = name


p1 = person()
p1.changename("rahul kumar")  # rahul kumar is passed in changename funtion
print(
    p1.name
)  # class method has access to make changes dirctly in class like it changes name variable
print(person.name)  # to rahul kumar replacing 'anonymous'




# important for class method


class person:
    a=1         #third priority
    def __init__(self):
        # self.a=a
        pass
    def change(self,a):
        # self.a=a
        pass

e1=person()    #second priority
# e1.a=45         #first priority
print(e1.a)


# 


class person:
    a=1         #third priority always 
    @classmethod
    def change(cls,a):
        cls.a=a

e1=person()    #second priority in self case 
e1.a=45         #first priority always
e1.change(6)       #second priority in cls case 
print(e1.a)



# 


class person:
    a=1        #want to access this 
    @classmethod
    def change(cls):
        print(cls.a)

e1=person()    
e1.a=45         
print(e1.a) #45
e1.change()  #1 



###########################
# @propertymethod
class student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        self.percentage = str((phy + chem + maths) / 3) + "%"

s1 = student(96, 94, 98)
print(s1.percentage)  # here percentage dont change even after change in phy number  # op =96%
s1.phy = 80
print(s1.phy)           # op is 80
print(s1.percentage)    #but percentage here is still 96% 
############
class student:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
    def newpercentage(self):    #this method is good but to do it better we use property method
        return str((self.phy +self.chem+self.maths)/3)+'%'      #when attribute value(percentage) depends on funtion ,
                                                                # we can make it a property means attribute that why propert is used

s1=student(96,94,98)
print(s1.newpercentage())       # 96%
s1.phy=80
print(s1.newpercentage())       # 90.6667%
#############################################################
# so to overcome this problem we use @property method
# use of property method
class student:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
    @property
    def newpercentage(self):                    
        return str((self.phy +self.chem+self.maths)/3)+'%'

s1=student(96,94,98)
print(s1.newpercentage)         # when attribute value(percentage) depends on funtion (newpercentage),
s1.phy=80                       # we can make it a property means attribute that why property is used,thats why curly braces are not written 
print(s1.newpercentage)         #curly braces are not allowed in this function after writing percentage()  no,() only percentage
#################################



class person:
    @property
    def fullname(self):
        return self.ename

p1=person()    
p1.ename="naman"
print(p1.ename)
print(p1.fullname)


# 323525

class person:
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]    # fname=first name split the name befor blank spaceand stores in  fname 
        self.lname = value.split(" ")[1]    # after that lname goes to do same 


p1 = person()
p1.name = "naman dua"       # .name is calling property  name of object p1
print(p1.fname, p1.lname) 