#In this exercise we covered-
# checking data type using type() method
# type casting, e.g. int("12")

#Type Checking
print(type(123_456))
print(type(123))
print(type("Tom"))
print(type(True))
print(type(123_56.234))
print()

#Type Conversion
# Make this line of code run without errors
# print("Number of letters in your name: " + len(input("Enter your name")))
print("Number of letters in your name: " + str(len(input("Enter your name\n"))))
print()

# int("abc") will give error because "abc" us invalid literal for int()

#print (1 + "2") gives error
print("1" + "2") #this is example of string concatenation
print(int("1") + int("2")) #this is example of adding two integers
