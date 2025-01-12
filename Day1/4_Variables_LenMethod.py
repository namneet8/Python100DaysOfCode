# Topics covered include-
# Creating a variable and storing input by user in it
# Using len() method to length of a String 
# Interchanging values of 2 variables using a 3rd variable

#creating a variable and storing user's input
name = input("What is your name?")
print(name)
print()

#the value in a variable can be changed at any time of the code
name = "Tom"
print(name)
print()

#using the length function to check length of user's input
#print("The length of user's input is " + len(input("What is your name?")))
# above line will give error because when we do concatenation, it expects a string but len function returns an int
print(len(input("What is your name?")))
print()

#creating separate variables for above step
username = input("What is your name?")
length = len(username)
print(length)
print()

#len(123456) won't work because length method only accepts Strings

# We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. 
# Write 3 lines of code to switch the contents of the variables. 
# You are not allowed to type the words "milk" or "juice". You are only allowed to use variables to solve this exercise.
glass1 = "milk"
glass2 = "juice"

temp = "milk"
glass1 = glass2
glass2 = temp
print(glass1)
print(glass2)