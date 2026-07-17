set ={1,2,3,4}
print(set)
print(type(set))

# {1, 2, 3, 4}
# <class 'set'>

# null set 
set = set()

print(set)
print(type(set)) 

# methods
collection = set()
# adds only one element in one statement
collection.add(33)
collection.add("naman")
collection.add(9.8)

print(collection)

# remove method
collection = set()
collection.add(33)
collection.add("naman")

collection.remove(33)
print(collection)

collection = {2,4,5,"harry"}
collection.remove(4)
print(collection)

# clear method removes all elements
collection = {2,4,5,"harry"}
collection.clear()
print(collection)


# pop method removes random element

collection = {2,4,"harry",5}
collection.pop()
print(collection)

collection = {2,4,"harry",5}
print(collection.pop())
print(collection)

# sets union method
set = {2, 4, "harry", 5}
set2 = {33, 44}
print(set.union(set2))  #new set will be returned no change in original set

# sets intersection method
set = {2, 4, "harry", 5}
set2 = {33,4}
print(set.intersection(set2))