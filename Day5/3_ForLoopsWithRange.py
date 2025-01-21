# This code doesn't do anything by itself. For example, if you tried to print it, it would not give you individual numbers.
print(range(1, 10))

# But it can be used in conjunction with For Loops. e.g.
for number in range(1, 10):
    print(number)
# This will print out each of the numbers 1 - 9. So the range can also be expressed like this:
# a <= range(a, b) < b

# Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.
total = 0
for n in range(1, 100+1):
    total += n
print(total)

# you can also specify step size in range
for number in range(1, 10, 2):
    print(number)