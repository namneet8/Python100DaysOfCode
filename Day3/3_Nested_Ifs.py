#nested if-else practice
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
