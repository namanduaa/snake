# string functions can work inside (print) statement 
# list functions not work inside print statement
# tuple functions can work inside (print) statement 
# dictionary functions outside print statement
# sets functions some ouside, some inside


a=(input("enter the name:"))
print(f"my name is : {a}")
#
print(r"C:\Users\naman")
# r is used to prevent unicode error
# r makes sure that \ in this is uses as normal character 
# otherwise it will be seen as \u or \N  which will cause error in this case 
# because \u and \n doesnot make ant sense
print("C:\\Users\\Naman")
# backslash is used because to print single slash
# output =C:\Users\Naman
a="namanam\"wf\"uuf"
print(a) # namanam"wf"uuf
#
name = input("enter your name=")
date = int(input("enter the date="))
letter = f"""
dear {name};
You are selected!
{date}
"""
print(letter)
# 


name = input("enter the name :")
print(f"Good afternoon {name}")
# 


letter = "dear <|name|>.\
  You are selected.\
<|Date|> "  #replace 
print(letter.replace("<|name|>", "naman").replace("<|Date|>", "18th may 2026"))
#


name = input("enter the name:")
date = input("enter the date:")
letter = f"dear {name}.\nYou are selected.\n{date}"
print(letter)
#


a="123.47"
print(a[3]) #output is dot (.)
#


