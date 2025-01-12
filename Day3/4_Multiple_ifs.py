# Write a program where an individual is only allowed to take a ride if their height is not less than 120cm.
# The ticket pricing is as follows-
# kids(12 or under)- $5
# teens(13-18)- $7
# adults- $12
# Also, they have option to buy photos and there is additional $3 for the photos.
# Print the final bill for the user.


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
    if buy_photo == "Y":#no need to create an else for this...
        bill += 3

    print(f"Your Final Bill is ${bill}") 
else:
    print("Sorry you have to grow taller before you can ride.")