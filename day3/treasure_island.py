print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
checkpoint1 = input("You arrive at a crossroad and have to choose a path. Do you want to go left or right?? ")
if checkpoint1 == "left" or checkpoint1 == "Left":
    checkpoint2 = input("You reached a lake!! Do you want to swim or wait?? ")
    if checkpoint2 == "swim" or checkpoint2 == "Swim":
        print("The lake was full of crocodiles!!")
        print("Game Over!")
    elif checkpoint2 == "wait" or checkpoint2 == "Wait":
        print("OH Wait!! Theres a boat service here. You pay him one full gold coin and cross the river safely!!")
        print("Theres now three shiny colourful doors to choose from. Only one of them leads to the treasure. Choose carefully!")
        checkpoint3 = input("Which door do you choose? ")
        if checkpoint3 == "red" or checkpoint3 == "Red":
            print("You drown in lava!!")
            print("Game Over!")
        elif checkpoint3 == "yellow" or checkpoint3 == "Yellow":
            print("Congratulations! You found the treasure!")
            print("You WIN!!")
        elif checkpoint3 == "blue" or checkpoint3 == "Blue":
            print("You just entered into a room full of snakes!!")
            print("Game Over!")
        else:
            print("Game Over!")
    else:
        print("Game Over!")

elif checkpoint1 == "right" or checkpoint1 == "Right":
    print("You have entered the lions den. Alas the lion hasn't eaten in days!!")
    print("Game Over!")

else:
    print("Game Over!")




