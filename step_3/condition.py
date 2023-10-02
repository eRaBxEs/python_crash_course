

cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
	if car == 'bmw':
		print(car.upper())

	else:
		print(car)


# Check whether a value exists in a list 
requested_toppings = ["mushrooms", "onions", "pineapples"]
print("mushrooms" in requested_toppings)
print("pepperoni" in requested_toppings)

# Another example of list checking
banned_users = ["andrew","carolina", "david"]
user = "marie"
if user not in requested_toppings:
	print(f"{user.title()}, you can post a response if you wish")
