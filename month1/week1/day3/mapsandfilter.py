numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["riddhi", "rohan", "priya", "amruta"]

# ---- MAP ----
# apply a function to every element

# square every number
squared = list(map(lambda x: x ** 2, numbers))
print("Squared:", squared)

# uppercase every name
upper_names = list(map(lambda n: n.upper(), names))
print("Upper:", upper_names)

# add 10 to every number
added = list(map(lambda x: x + 10, numbers))
print("Added 10:", added)


# ---- FILTER ----
# keep only elements that match a condition

# keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)

# keep only odd numbers
odds = list(filter(lambda x: x % 2 != 0, numbers))
print("Odds:", odds)

# keep only names longer than 5 characters
long_names = list(filter(lambda n: len(n) > 5, names))
print("Long names:", long_names)


# ---- MAP + FILTER COMBINED ----
# filter evens first, then square them
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print("Even squares:", result)