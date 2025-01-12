#In python input() method is used to take input, where in brackets we type the string that will be visible on console

#input("What is your name?")-> this statement returns the input given by user 
#and hence can be printed through print method
print(input("What is your name?\n")) #add \n at the end of the string to get cursor on next line
print()

#combining String Concatenation and input() method
#Since input() method returns a String it can be used in string concatenation
print("Hello " + input("What is your name?\n") + "! How are you?")