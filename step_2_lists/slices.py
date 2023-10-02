my_foods= ["pizza", "falafel", "carrot cake"]
my_friend_foods = my_foods[:]
baby_foods = my_foods # NB. Any change that happens on my_foods affects baby_foods and vice versa

# Printing all individual food
print(my_foods)
print(my_friend_foods)
print(baby_foods)

# append to some of the list
my_foods.append("cannoli")
my_friend_foods.append("ice cream")

# print them all
print(my_foods)
print(my_friend_foods)
print(baby_foods) # in printing to output, one will observe that my_foods and baby_foods both have the same contents.

# Now append data to baby_foods
baby_foods.append("cereals")
print(baby_foods)
print(my_foods)
