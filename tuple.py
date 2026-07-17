# tuple concatenation using + in print
a=(1,3,5,False)
b=(2,4,6)
print(a+b)  


#
a=(1,3,5,False)  #repetetion
print(a*3) # print tuple 3 times


#
a=(1,3,5,False) #membership
print(3 in a) # checks if element is present in tuple or not = true,false


#
a=(1,3,5,False)
print(len(a))


#
a=(1,3,5,False)
print(a[1:3]) #slicing in tuples  create a new tuple ou of original
print(a)


#
a=(1,3,5,False)
b,c,d,e=a  #unpacking in tuple is assigning values of tuple in differet variable
print(b,c,d,e)  # too many values to unpack if variable s are less than total no .of value in tuple
print(a)    
#ValueError: not enough values to unpack if more variables than values in tuples