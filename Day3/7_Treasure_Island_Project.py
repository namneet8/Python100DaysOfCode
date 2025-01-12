#notice the use of print ('''   '''), upper(), lower()
#see the flow chart for this exercise


print('''
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
left_or_right = input("Do you want to go to left or right? Enter L or R\n").upper()
if left_or_right == "R":
    print("Oh no!!! You got hit by a truck. Game Over")
elif left_or_right == "L":
    swim_or_wait = input("Do you want to swim or wait? Enter S or W\n").upper()
    if swim_or_wait == "S":
        print("Oh no!!! You got eaten by a crocodile. Game Over")
    elif swim_or_wait == "W":
        door_color = input("Which door colour do you want to go through? Enter Y for yellow, R for red and B for Blue\n").upper()
        if door_color == "R" or door_color == "B":
            print("Oh no!!! You chose the door that goes to devil. Game Over")
        elif door_color == "Y":
            print("You Won!!!")
        else:
            print("you have typed wrong inputs")
    else:
        print("you have typed wrong inputs")
else:
    print("you have typed wrong inputs")