#You can create a simple collection of ordered items using a Python list. e.g.
fruits = ["Cherry", "Apple", "Pear"]
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#Accessing Items in Lists
#Items can be accessed by either positive indices ( 0 to len(list)-1 ) or negative indices ( -1 to -len(list) )
print(states_of_america[0])
print(fruits[-1])

#Modifying Items
fruits[0] = "Orange"
print(fruits)

#Adding Items
fruits.append("Banana")
print(fruits)

#list.extend(iterable)
# Adds all elements from an iterable (like a list, tuple, or string) to the end of the list.
# Unlike append, which adds the entire iterable as a single element, extend takes each element from the iterable and adds them individually.
fruits.extend(['Passion fruit', 'Dragon fruit', 'Kiwi' ])
print(fruits)
fruits.append(['Passion fruit', 'Dragon fruit', 'Kiwi' ])
print(fruits)

# list.insert(i, x)
# Inserts an element x at a specific index i in the list.
# If i=0, x is added at the very start of the list.
# If i equals the length of the list (len(list)) or a higher number, x is appended to the end (similar to append).
fruits.insert(0, "Watermelon")
print(fruits)
fruits.insert(2, "Muskmelon")
print(fruits)
fruits.insert(len(fruits)+1, "Muskmelon")
print(fruits)