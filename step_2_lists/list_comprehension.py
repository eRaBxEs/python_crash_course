# Using range in python
for value in range(1, 6):
	print(value)


# Creating a list of numbers using range and list functions
numbers = list(range(-7, 8))
print(numbers)

# Create even numbers as a list
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Squares of numbers 1 - 10
squares = []
for value in range(1, 11):
	squares.append(value ** 2)

print(squares)

# max, min and sum of a list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(max(digits))
print(min(digits))
print(sum(digits))

# Simple intro to List Comprehensionn
squared = [value ** 2 for value in range(1, 11)]
print(squared)

#  Cubes of numbers 1 - 10
cubes = []
for value in range(1, 11):
	cubes.append(value ** 3)
print(cubes)

# using List Comprehension for Cubes of number from 1 - 10
cubed = [value ** 3 for value in range(1, 11)]
print(cubed)

# Slices in python
players = ["charles", "martina", "michael", "florence"]
print(players[0:3])
print(players[2:])
print(players[:2])
print(players[:])
print(players[-3:])

# Looping thru a slice
print("Here are the first 3 players in my list")
for player in players[:3]:
	print(player.title())


