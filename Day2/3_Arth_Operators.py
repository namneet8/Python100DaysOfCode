#Learn to use the basic mathematical operators, +, -, *, /, // and **
#PEMDAS -> Parentheses, Exponents, Multiplication/Division(left most is solved first), Addition/Subtraction(left most is solved first)

#new operators
#// -> Floor division It removes the decimal from the result of a/b, e.g. 4/2 = 2.0 but 4//2 = 2
#** -> Exponent, e.g. 2**3 = 8

#What is the output of this code?
print(3 * 3 + 3 / 3 - 3)
# (3*3)+3/3-3 = 9+3/3-3 = 9+(3/3)-3 = 9+1.0-3 = (9+1.0)-3 = 10.0-3 = 7.0

# Change the code so it outputs 3?
# print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)
# 3*(3+3)/3-3 = 3*6/3-3 = (3*6)/3-3 = 18/3-3 = (18/3)-3 = 6.0-3 = 3.0

# Write your code here.
# Calculate the bmi using weight and height.
height = 1.65
weight = 84
bmi = weight/(height**2) #brackets are not necessary as ** has higher precedence than /

print(bmi)