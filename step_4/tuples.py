# Python refers to values that does not change as immutable, and an immutable list is called a tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Tuples are technically defined by the presence of a comma, see below:
dimensions_2 = 250, 20, 10
print(dimensions_2[0])
print(dimensions_2[1])
print(dimensions_2[2])

# Tuple with just one element
my_t = (3, )
print(my_t)

# Tuple is not modifiable, you can't change the elements of a tuple, but one can change the value of a variable that represents a tuple
print("Original dimensions")
for dimension in dimensions:
	print(dimension)

    
dimensions = (400, 25)
print("\nModified dimensions")
for dimension in dimensions:
	print(dimension)

