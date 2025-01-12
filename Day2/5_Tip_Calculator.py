#Create a tip calculator program that asks the user for bill amount, tip percentage and number of people to split the bill into.
#then prints out the per person bill after adding tip

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

bill += bill * (tip / 100) #or bill = bill * (1 + tip/100)
bill_per_person = round(bill/people, 2)
print(f"Each person should pay: ${bill_per_person}")