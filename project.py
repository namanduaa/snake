# In the Snake Water Gun game, players choose between three options: snake, water, and gun, with specific interactions determining the winner.
# Game Overview
# Players: The game is typically played between two players.
# Choices: Each player simultaneously chooses one of three options: snake, water, or gun.
# Winning Conditions
# Snake vs. Water: Snake drinks water, so the snake wins.
# Water vs. Gun: Water douses the gun, so water wins.
# Gun vs. Snake: Gun kills the snake, so the gun wins.
# Draw: If both players choose the same option, the game results in a draw.
# Summary of Interactions
# Snake: Wins against water but loses to gun.
# Water: Wins against gun but loses to snake.
# Gun: Wins against snake but loses to water.

dict = {
    "s":"snake" ,
    "w": "water" , 
    "g":"gun",
}

compchoice = input("computer choice:")   # enters the s , w , g
yourchoice = input("enter your choice :")  # enters the s , w , g

computer = dict[compchoice]  #computer stores snake,water,gun from dict 
you = dict[yourchoice]       #you stores snake,water,gun from dict 

if computer == "snake" and you == "water":   # computer,you checks snake,wwater ,gun
    print("computer wins the game.")
elif computer == "snake" and you == "gun":
    print("you wins the game.")

elif computer == "water" and you == "gun":
    print("computer wins the game.")
elif computer == "water" and you == "snake":
    print("you wins the game.")

elif computer == "gun" and you == "water":
    print("you wins the game.")
elif computer == "gun" and you == "snake":
    print("computer wins the game.")

elif computer == you:
    print("it is a draw")
else:
    print("--------crash---------")


##############################################################################


computer = input("computer choice:")  
you = input("enter your choice :")  


if computer == "snake" and you == "water":   
    print("computer wins the game.")
elif computer == "snake" and you == "gun":
    print("you wins the game.")

elif computer == "water" and you == "gun":
    print("computer wins the game.")
elif computer == "water" and you == "snake":
    print("you wins the game.")

elif computer == "gun" and you == "water":
    print("you wins the game.")
elif computer == "gun" and you == "snake":
    print("computer wins the game.")

elif computer == you:
    print("it is a draw")
else:
    print("--------crash---------")


#############################################################################

import random

dict = {
    1:"snake" ,
    -1: "water" , 
    0:"gun",
}
random_choice = random.choice([1,-1,0])  
yourchoice = int(input("enter your choice :"))

computer = dict[random_choice]  #computer stores snake,water,gun from dict 
print(f"computer random choice is : {random_choice}")
you = dict[yourchoice]       #you stores snake,water,gun from dict 

if computer == "snake" and you == "water":   # computer,you checks snake,wwater ,gun
    print("computer wins the game.")
elif computer == "snake" and you == "gun":
    print("you wins the game.")

elif computer == "water" and you == "gun":
    print("computer wins the game.")
elif computer == "water" and you == "snake":
    print("you wins the game.")

elif computer == "gun" and you == "water":
    print("you wins the game.")
elif computer == "gun" and you == "snake":
    print("computer wins the game.")

elif computer == you:
    print("it is a draw")
else:
    print("--------crash---------")

#############################################################################

import random
while True:
    choice = input("roll the dice (y/n) :")
    if choice.lower() == "y":
        number1 = random.randint(1, 6)
        number2 = random.randint(1, 6)
        print((number1, number2))

    elif choice.lower() == "n":
        break
    else:
        print("invalid")

################################################################

import random
number = random.randint(1, 100)
while True:
    try:
        guess = int(input("guess the number:"))
        if number > guess:
            print("too low")
        elif number < guess:
            print("too high")
        elif number == guess:
            print("congrats you guess is right")
            break
    except ValueError:
        print("enter a valid number")

############################################################

import random

while True:
    computer_choice = random.choice(["r", "p", "s"])
    user_choice = input("Rock, paper, scissor ?(r/p/s): ").lower()

    
    if user_choice not in ["r", "p", "s"]:
        print("invalid choice")
        continue
    
    if user_choice == computer_choice:
        print(f"computer choose {computer_choice}\nyou choose {user_choice}")
        print("it's a tie!")
    elif computer_choice == "r" and user_choice == "p":
        print("computer choose rock\nyou choose paper")
        print("you win")
    elif computer_choice == "r" and user_choice == "s":
        print("computer choose rock\n" "you choose scissor")
        print("you lose")
    elif computer_choice == "p" and user_choice == "r":
        print("computer choose paper\nyou choose rock")
        print("you lose")
    elif computer_choice == "p" and user_choice == "s":
        print("computer choose paper\nyou choose scissor")
        print("you win")
    elif computer_choice == "s" and user_choice == "r":
        print("computer choose scissor\nyou choose rock")
        print("you win")
    elif computer_choice == "s" and user_choice == "p":
        print("computer choose scissor\nyou choose paper")
        print("you lose")
    elif(user_choice==computer_choice):
        print("it is a tie")
        
    play_again = input("\nPlay again? (y/n): ")
    if play_again.lower() != "y":
        break

###############################################################

import random

# dict = {"r": "🪨", "p": "📋", "s": "✂️"}
while True:
    computer_choice = random.choice(["r", "p", "s"])
    user_choice = input("Rock, paper, scissor ?(r/p/s): ")
    dict = {"r": "🪨", "p": "📋", "s": "✂️"}
    if user_choice not in dict:
        print("invalid choice")
        continue

    if user_choice == computer_choice:
        print(f"computer choose {dict[computer_choice]}\nyou choose {dict[user_choice]}")
        print("it's a tie!")
    elif computer_choice == "r" and user_choice == "p":
        print(f"computer choose {dict[computer_choice]}\nyou choose {dict[user_choice]} ")
        print("you win")
    elif computer_choice == "r" and user_choice == "s":
        print(f"computer choose {dict[computer_choice]}\n" "you choose  {dict[user_choice]}")
        print("you lose")
    elif computer_choice == "p" and user_choice == "r":
        print(f"computer choose  {dict[computer_choice]}\nyou choose {dict[user_choice]}")
        print("you lose")
    elif computer_choice == "p" and user_choice == "s":
        print(f"computer choose {dict[computer_choice]} \nyou choose {dict[user_choice]}")
        print("you win")
    elif computer_choice == "s" and user_choice == "r":
        print(f"computer choose  {dict[computer_choice]}\nyou choose {dict[user_choice]}")
        print("you win")
    elif computer_choice == "s" and user_choice == "p":
        print(f"computer choose  {dict[computer_choice]}\nyou choose {dict[user_choice]}")
        print("you lose")
    elif user_choice == computer_choice:
        print("it is a tie")

    play_again = input("\nPlay again? (y/n): ")
    if play_again.lower() != "y":
        break






#




import random

while True:
    computer_choice = random.choice(["r", "p", "s"])

    user_choice = input("Rock, paper, scissor ?(r/p/s): ")

    dict = {"r": "🪨", "p": "📋", "s": "✂️"}

    if user_choice not in dict:
        print("invalid choice")
        continue
    print(f"computer choose{dict[computer_choice]}")
    print(f"you choose{dict[user_choice]}")

    if user_choice == computer_choice:
        print("it's a tie!")
    elif(user_choice=="r" and computer_choice=="s") or (user_choice=="s" and computer_choice=="p") or (user_choice=="p" and computer_choice=="r"):
        print("you win")
    else:
        print("you lose")


    play_again=input("want to play again(y/n?").lower()
    if play_again != "y" :
        break





#





import random
dict = {"r": "🪨", "p": "📋", "s": "✂️"}
choices=("r","p","s")
def getuserchoice():
    while True:
        userchoice=input("rock. paper,scissor?").lower()
        if userchoice in choices:
            return userchoice
        else:
            print("invalid choice")

def displaychoices(userchoice,computerchoice):
    print(f'you chose {dict[userchoice]}')
    print(f'computer chose {dict[computerchoice]}')

def determinewinner(userchoice,computerchoice):
    if userchoice==computerchoice:
        print('tie')
    elif((userchoice=="r" and computerchoice=="s") or (userchoice=="s" and computerchoice=="p") or (userchoice=="p" and computerchoice=="r")):
        print('you win')
    else:
        print('you lose')

def playgame():
    while True:
        userchoice= getuserchoice
        computerchoice=random.choice(choices)

        displaychoices(userchoice,computerchoice)
        determinewinner(userchoice,computerchoice)

        shouldcontinue=input("continue(y/n)?").lower()
        if shouldcontinue !='y':
            break
        
playgame()




#




import random

ROCK='r'
PAPER='p'
SCISSORS='s'

dict = {ROCK: "🪨", PAPER: "📋", SCISSORS: "✂️"}
choices=tuple(dict.keys())
def getuserchoice():
    while True:
        userchoice=input("rock. paper,scissor?").lower()
        if userchoice in choices:
            return userchoice
        else:
            print("invalid choice")

def displaychoices(userchoice,computerchoice):
    print(f'you chose {dict[userchoice]}')
    print(f'computer chose {dict[computerchoice]}')

def determinewinner(userchoice,computerchoice):
    if userchoice==computerchoice:
        print('tie')
    elif((userchoice==ROCK and computerchoice==SCISSORS) or (userchoice==SCISSORS and computerchoice==PAPER) or (userchoice==PAPER and computerchoice==ROCK)):
        print('you win')
    else:
        print('you lose')

def playgame():
    while True:
        userchoice= getuserchoice()
        computerchoice=random.choice(choices)

        displaychoices(userchoice,computerchoice)
        determinewinner(userchoice,computerchoice)

        shouldcontinue=input("continue(y/n)?").lower()
        if shouldcontinue !='y':
            break
        
playgame()




##########################################################333



# qr code generator

import qrcode

data = input("enter the url of site :")  # name of url you want to make qrcode of

filename = input(
    "enter the name of file you want :"
)  # name of file wherer picture of qr will be stored

qr = qrcode.QRCode(box_size=10, border=5)
qr.add_data(data)

image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)
print(f"QR CODE saved as {filename}")




#


import random

target = random.randint(1, 100)

while True:
    try:
        guess = int(input("guess the number: "))
        if guess < target:
            print("low guess")
        elif guess > target:
            print("high guess")
        elif guess == target:
            print("congratulations")
            break
    except ValueError:
             print("invalid number")




#



# password genarator

import random
import string

n = int(input("enter the length of password :"))
list = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(n):
    password += random.choice(list)

print(password)


# 



import random
import string

n = int(input("enter the length of password :"))
list = string.ascii_letters + string.digits + string.punctuation
def choose():
    password = ""
    for i in range(n):
        password += random.choice(list)
    print(password)

choose()


# 



import random
import string

n = int(input("enter the length of password :"))
chars = string.ascii_letters + string.digits + string.punctuation
password=""
newlist=[]
for i in range(n):
    password=random.choice(chars)
    newlist+=password

print(newlist)


# 

# list comprehensio used when we need to call function continously and stores its values in list

import random
import string

n = int(input("enter the length of password :"))
chars = string.ascii_letters + string.digits + string.punctuation

password=[random.choice(chars) for i in range(n)]

# password=""
# newlist=[]
# for i in range(n):
#     password=random.choice(chars)
#     newlist+=password

print(password)



# 



import random
import string

n = int(input("enter the length of password :"))
chars = string.ascii_letters + string.digits + string.punctuation

password="".join([random.choice(chars) for i in range(n)])

# password=""
# newlist=[]
# for i in range(n):
#     password=random.choice(chars)
#     newlist+=password

print(password)