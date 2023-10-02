# Looping through a list using for loop 
animals = ["cat", "dog", "rat", "goat", "sheep", "lion", "tiger", "cow", "python"]
print(animals)

print(animals[0], animals[1], animals[2], animals[3], animals[4], animals[5])

# Loop
for animal in animals:

	print(animal, ": Is an animal I have seen")
	prefer = f"Will you prefer {animal} as a pet"
	print(prefer)

print("Done with the list of animals")
print("\n\n\n")

# Loop 2:
numbers = [3, 5, 7, 2, 9]
for num in numbers:
	print(num, "is in the list")
print("Done!")

# Loop 3:
for value in range(1, 8):
	print(value)


numbers_list = []
print("Before Loop using range: ", numbers_list)

# Loop 4:
for value in range(1, 11):
	numbers_list.append(value)
print("After Loop using range: ", numbers_list)

print("\n\n")

even_numbers = []
print("Before Loop using range: ", even_numbers)
# Loop 5:
for value in range(2, 11, 2):
	even_numbers.append(value)

print("After Loop using range: ", even_numbers)


print("\n\n")
odd_numbers = []
print("Before Loop using range: ", odd_numbers)
for odd in range(1, 20, 2):
	odd_numbers.append(odd)

print("After Loop using range: ", odd_numbers)



# Assignment 1
# Create a list of food you like
# Use for Loop to loop through them printing the name of the food.

# Assignment 2
# Create a list of squares of numbbers from 1 to 10
# Loop through them.







