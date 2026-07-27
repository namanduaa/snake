dict = {
    "name": "naman",
    "cgpa": 9.2,
    "marks": [98, 99, 97],
    "0": "harry",
}

dict["class"] = 12
dict["name"]="somnath"
print(dict)  # printing full dictionary content 
# {'name': 'naman', 'cgpa': 9.2, 'marks': [98, 99, 97], '0': 9}


print(dict["cgpa"]) #normal way of printing 
# just write key name and value will bw prinnted




# null dictionary
empdict={}
print(empdict)   



nulldict={}
nulldict["name"]="naman""aman" #if comma not present
print(nulldict["name"])    #output namanaman
 
#if comma present it is presented as tuple 
nulldict={

}
nulldict["name"]="naman","aman"
print(nulldict["name"])    #output = ('naman', 'aman')


# normal
nulldict={}
nulldict["name"]="naman"
nulldict["class"]=12
print(nulldict)
# output {'name': 'naman', 'class': 12}



###########nested dictionary#####################
dict1 = {
    "name": "naman",
    "class": 12,
    "marks": {
        "physics": 45,
        "chemistry": 67,
        "biology": 77,
    },
    "cgpa": 9.7,
}

print(dict1["marks"]["chemistry"]) #67



########## methods in dictionary ####################### 
dict = {
    "name": "naman",
    "class": 12,
    "physics": 45,
    "chemistry": 67,
    "biology": 77,
    "cgpa": 9.7,
}
print(dict.keys())
# dict_keys(['name', 'class', 'physics', 'chemistry', 'biology', 'cgpa'])
# doesnot print key inside of nested dictionary
# <class 'dict_keys'>
###############
print(list(dict.keys())) 
# dict keys converted into list of keys


print(len(list(dict.keys()))) #4

print(len(dict)) #4



dict = {
    "name": "naman",
    "class": 12,
    "marks": {
        "physics": 45,
        "chemistry": 67,
        "biology": 77
    },
    "cgpa": 9.7,
}
print(dict.values())



dict = {
    "name": "naman",
    "class": 12,
    "marks": {
        "physics": 45,
        "chemistry": 67,
        "biology": 77
    },
    "cgpa": 9.7,
}
print(dict.items())
# returns key value pairs as tuples


dict = {
    "name": "naman",
    "class": 12,
    "marks": {
        "physics": 45,
        "chemistry": 67,
        "biology": 77,
    },
    "cgpa": 9.7,
}
print(len(dict.items()))


#
dict = {
    "name": "naman",
    "class": 12,
    "marks": {
        "physics": 45,
        "chemistry": 67,
        "biology": 77,
    }
}  
print("before")
print(dict.get("name2"))
print('after')
# we use get because it gives none as result if key's name is not present
# it allows other code to run 
# but in normal calling it stops th whole code from working
dict = {
    "name": "harry",
    "class": "12th",
    "marks": {
        "phy": 44,
        "chem": 56,
    },

    "rollno": 22,
}
print(dict.get("class"))
# 12th


dict = {
    "name": "naman",
    "class": 12,
    "marks": {
        "physics": 45,
        "chemistry": 67,
        "biology": 77,
    }
}
dict.update({"cgpa":9.8})
print(dict)






# updating dictionary 
dict = {
    "name": "naman",
    "class": 12,
    "marks": {
        "physics": 45,
        "chemistry": 67,
        "biology": 77,
    }
}
dict.update({"cgpa":9.8,"roll no":11})
print(dict)
# {'name': 'naman', 'class': 12, 'marks': {'physics': 45, 'chemistry': 67, 'biology': 77}, 'cgpa': 9.8, 'roll no': 11}

dict = {
    "name": "naman",
    "class": 12,
    "marks": {
        "physics": 45,
        "chemistry": 67,
        "biology": 77,
    },
}
newdict = {
    "city": "delhi",
    "name":"somanth"
}
dict.update(newdict)   #new dict added into dict and name is updated 
print(dict)

# {'name': 'somanth', 'class': 12, 'marks': {'physics': 45, 'chemistry': 67, 'biology': 77}, 'city': 'delhi'}



dict = {
    "name": "harry",
    "class": "12th",
    "marks": {
        "phy": 44,
        "chem": 56,
    },

    "rollno": 22,
}
print(list(dict))
# ['name', 'class', 'marks', 'rollno']
# default behaviour

