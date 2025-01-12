print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?\n"))
    if age <= 12:
        bill  = 5
        print(f"Child Tickets are ${bill}.")
    elif age <= 18:
        bill = 7
        print(f"Youth Tickets are ${bill}.")
    else:
        bill = 12
        print(f"Adult Tickets are ${bill}.")
    buy_photo = input("Do you want photos? Enter Y or N\n")
    if buy_photo == "Y":
        bill += 3

    print(f"Your Final Bill is ${bill}") #no need to create an else for this...
else:
    print("Sorry you have to grow taller before you can ride.")