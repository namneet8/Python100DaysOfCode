import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#Method 1
rand_n = random.randint(0, len(friends)-1)
print(friends[rand_n] + " will pay the bill.")

#Method 2
print( random.choice(friends) + " will pay the bill.")