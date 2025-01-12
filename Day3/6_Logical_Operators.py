# A and B 
# C or D 
# not E 

# Write a program where an individual is only allowed to take a ride if their height is not less than 120cm.
# The ticket pricing is as follows-
# kids(12 or under)- $5
# teens(13-18)- $7
# adults- $12
# But, for people in age group 45- 55, the ride is free.
# Also, they have option to buy photos and there is additional $3 for the photos.
# Print the final bill for the user.
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55: #can also be written as:-  elif 45 <= age <= 55:
        #bill = 0 not needed....
        print("You can ride for free")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
