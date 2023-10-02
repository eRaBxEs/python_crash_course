# list of animals :: comments are not executed as part of your code flow
animals = ["cat", "dog", "rat", "goat", "sheep", "lion", "tiger", "cow", "python"]
length_animals = len(animals)
print("The length of the list above:", length_animals) 

print("Before reversing :",animals)
print(animals[0])
print(animals[8])
print(animals[-1], ": Gets you the last item in a list no matter the size of the list")
print(animals[-3])

animals.reverse() ## using reverse method
print("After reversing :", animals)

