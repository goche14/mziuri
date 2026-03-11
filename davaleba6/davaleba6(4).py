import random

chance = 5

print("you have to ges pin you have 5 trys good luck ")
pin = random.randint(1000,10000)
guess1 = int(input("enter 4 digit pin: "))
    
if guess1 == pin:
    print("correct")
elif guess1 != pin:
    print("you have 4 trys guess again: ")
    chance = chance - 1

guess2 = int(input("enter 4 digit pin: "))
    
if guess2 == pin:
    print("correct")
elif guess2 != pin:
    print("you have 3 trys guess again: ")
    chance = chance - 1

guess3 = int(input("enter 4 digit pin: "))
    
if guess3 == pin:
    print("correct")
elif guess3 != pin:
    print("you have 2 trys guess again: ")
    chance3 = chance - 1

guess4 = int(input("enter 4 digit pin: "))
    
if guess4 == pin:
    print("correct")
elif guess4 != pin:
    print("you have 1 trys guess again: ")
    chance = chance - 1

guess5 = int(input("enter 4 digit pin: "))
    
if guess5 == pin:
    print("correct")
elif guess5 != pin:
    print("blocked! you have no more guesses ")
    
