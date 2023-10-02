# list : Idea of a list
					
names_of_people = ["jack", "Bill", "Games", "Leane"]
cars = []

# methods and fuctions that are useful in managing our list
# methods : insert, append, remove, pop, sort
# function : sorted

print(names_of_people)
print(cars)

#names_of_people.insert("jude")

print(names_of_people[0])

print(names_of_people[1])

print(names_of_people[2])

print(names_of_people[3])

print(names_of_people[-1])


names_of_people.insert(0, "jude")
names_of_people.insert(2, "jesus")



print(names_of_people)



# append
cars.append("toyota")
cars.append("nissan")
cars.append("lexus")
print(cars)


# remove
cars.remove("nissan")
print(cars)
cars.remove("toyota")

# pop
popped_out = names_of_people.pop()
print(popped_out)
print(names_of_people)

popped_again = names_of_people.pop(1)
print(popped_again)
print(names_of_people)

# sort // alphabetically
names_of_people.sort()
print("Alphabetical sorting: ", names_of_people)
names_of_people.sort(reverse=True)
print("Reverse sorting:", names_of_people)



# sorted()
sorted_names = sorted(names_of_people)
print("Sorted variable:", sorted_names)
print("Main list remain unchanged: ", names_of_people)




