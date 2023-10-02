# Printing a literal string
print("Hello Python Gracey!")

# print is a function used to display to an output
print("Something here. Anything comes in here!")

# variables are more like a container that stores a defined type of data
first_name_1 = "petra" # string can either be in double quotes or single quote
last_name_1 = 'onifade'
age = 12  # number : integer
money = 30.50 # number : float

print(first_name_1)
print(last_name_1)
print(age)

 # using the title method for a string variable
print(first_name_1.title()) 
print(last_name_1.title())

 # using the method upper to convert a string to upper case 
first_name = first_name_1.upper()
last_name = last_name_1.upper()
print(first_name)
print(last_name)

# using the method lower to convert strings to lower case
small_first = first_name.lower()
small_last = last_name.lower()
print(small_first)
print(small_last)

# formatting a string in python 3.6 and above
full_name = f"first name: {first_name} last name: {last_name}"
print(full_name)

greet = f"Greetings, {first_name_1} {last_name_1}, you passed your exams"
print(greet)




# formatting a string in python 3.5 and below using the format method
full_name_2 = "first name:{} last name: {}".format(first_name, last_name)
print(full_name_2)

greet2 = "Greetings, {} {}, you passed your exams".format(first_name_1,last_name_1)
print(greet2)





