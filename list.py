a = [88, 8, 9, 12, 33]
a.pop(2)
print(a)
# [88, 8, 12, 33] output
# it will return a output after delecting value at index (2)

a = [88, 8, 9, 12, 33]
print(a.pop(2))
# it will return the value which the  pop keyword is removing from list.
# which is 9 in this case at index 2
#

a = [88, 8, 9, 12, 33]
print(sorted(a)) #sorted doesnot not make changes in actual  list (a).
print(a) # sort does
#
a = [88, 8, 9, 12, 33]
a.sort()
print(a) #sort changes list and does its work 
#
# but sort in print function returns none 
# So print(a.sort()) prints None because that's what the method returns,
a = [88, 8, 9, 12, 33]
print(a.sort())
#


# l1 = [1,8,7,2,21,15] 
# • l1.sort(): updates the list to [1,2,7,8,15,21] 
# • l1.reverse(): updates the list to [15,21,2,7,8,1] 
# • l1.append(8): adds 8 at the end of the list  
# • l1.insert(3,8): This will add 8 at 3 index
# • l1.pop(2): Will delete element at index 2 and return its value. 
# • l1.remove(21): Will remove 21 from the list.