
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Rock! Paper! Scissors!")

#getting user's choice
user_choice = int(input("Please Type 0 for Rock, 1 for Paper and 2 for Scissors: "))

#getting computer's choice
import random
comp_choice = random.randint(0,2)

#printing out hands for user and computer by creating a list and using choice number as index
hand_gestures = [rock, paper, scissors]
if user_choice >= 0 and user_choice <= 2:
    print("You chose: ")
    print(hand_gestures[user_choice])

print()
print("Computer chose: ")
print(hand_gestures[comp_choice])

#Game rules
if user_choice < 0 or user_choice > 2:
    print("You lose! You inputted wrong number.")
elif user_choice == comp_choice:
    print("It's a draw.")
elif (comp_choice == 0 and user_choice == 1) or (comp_choice == 1 and user_choice == 2) or (comp_choice == 2 and user_choice == 1):
    print("You win.")
else:
    print("You Lose.")

#Method 2
if user_choice < 0 or user_choice > 2:
    print("You lose! You inputted a wrong number.")
else:
    result = (user_choice - comp_choice) % 3
    if result == 0:
        print("It's a draw.")
    elif result == 1:
        print("You win.")
    else:
        print("You lose.")

# Case 1: User wins
# i) Comp - 0 User-1 -> (1-0)%3 = 1%3 = 1
# ii) Comp- 1 User-2 -> (2-1)%3 = 1%3 = 1
# iii) Comp-2 User-0 -> (0-2)%3 = -2%3 = 1          3)-2(-1
#                                                     -3
#                                                      1    -2 - (-3) = 1
# Case 2: Comp wins
# i) Comp - 0 User-2 -> (2-0)%3 = 2%3 = 2
# ii) Comp- 1 User-0 -> (0-1)%3 = -1%3 = 2
# iii) Comp-2 User-1 -> (1-2)%3 = -1%3 = 2         -1 - (-3) = 2
# 
# Case 3: Draw
# i) Comp - 0 User-0 -> 0%3 = 0
# ii) Comp- 1 User-1 -> 0%3 = 0
# iii) Comp-1 User-1 -> 0%3 = 0  