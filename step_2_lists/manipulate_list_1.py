# Introduction to List

car_models = ["benz", "nissan", "toyota"]
person = [] # empty list

# methods and functions that can be used to manipulate a list
# index number
print(car_models[0])
print(car_models[1])
print(car_models[2])

print("The number of items in list car_models is ", len(car_models)) # len() : function
print("The number of items in list person is ", len(person)) # len() : function

# method :: append()
car_models.append("lexus")
car_models.append("jaguar")
print(car_models)

person.append("boy")
person.append("girl")
person.append("baby")
print(person)

# method :: insert(index, value)
person.insert(1, "mummy")
print(person)
person.insert(2, "daddy")
print(person)

# delete statement : is used to delete from a list
del car_models[0]
del car_models[0]
print(car_models)

# pop : : method : by default pops out the last element in the list
popped_item = person.pop()
print(person)
print(popped_item)

popped_item_2 = person.pop(2)
print(person)
print(popped_item_2)

# remove : removes an item
car_models.remove("jaguar")
print(car_models)


num_list = [10, 4, 2, 5, 7]

# sort : : it is used to arrange ascending order
person.sort()
print(person)

print("Before sorting: ", num_list)
num_list.sort()
print("After sorting: ", num_list)

# sort : : method ::  descending order
num_list.sort(reverse = True)
print("After sorting in descending order", num_list)

# sorted : : function sorted()
num2_list = [5, 12, 4, 8]
sorted_list = sorted(num2_list) # sorted in ascending order
print(sorted_list)
print(num2_list)

print("something")


animals = ["rat", "goat", "dog", "cat", "sheep"]
print("Before reversing :",animals)
# reverse : : method
animals.reverse()
print("After reversig :",animals)








