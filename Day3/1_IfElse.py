#In this exercise we covered, If else and Comparison Operators
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to

# Write a program for a rollercoaster ride, where you are allowed to take a ride if your height is 120 cm or more.
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("Hurray! You can ride the rollercoaster!!")
else:
    print("Sorry, You can't ride the rollercoaster.")
print()

#Single If statement
if 5 > 2: #This is a parent line of code
    print("yes") #this is a child line of code
print()

# demo of using ==
if 6/2 == 3:
    print("it is 3")
else:
    print("it is not 3")