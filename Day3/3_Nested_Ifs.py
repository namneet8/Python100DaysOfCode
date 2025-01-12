#nested if-else practice

# 1. Write a program where you are only allowed to ride a rollercoaster if your height is not less than 120 cm.
# Also, for kids (18 or under) the ticket price is $7 while adults is $12
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age > 18 :
        print("Please pay $12 at the ticket counter.")
    else:
        print("Please pay $7 at the ticket counter.")
else:
    print("Sorry you have to grow taller before you can ride.")
print()

# nested if else and elif practice

# 2. Write a program where only people with height 120 or more are allowed to take a rollercoaster ride. 
# Also, for kids (12 or under) ticket costs $5, for teens (13-18) ticket costs $7, for adults tickst costs $12

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 12:
        print("Please pay $5 at the ticket counter.")
    elif age <= 18:
        print("Please pay $7 at the ticket counter.")
    else:
        print("Please pay $12 at the ticket counter.")
else:
    print("Sorry you have to grow taller before you can ride.")
print()

# bmi example
#Write a program to calculate bmi from given weight and height, weight = 85 and height = 1.85. Formula- W/H^2
#if bmi is less than 18.5, print underweight
#if bmi is between 18.5-24.9, print normal weight
#if bmi is greater than 24.9, print overweight
weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi <= 24.9:
    print("normal weight")
else:
    print("overweight")
print()
