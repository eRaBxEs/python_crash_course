# interesting things with string
name = "ada lovelace"
new_name = name.title()
upper_name = name.upper() # what is the function doing
lower_name = name.lower() # what is the function doing
#name_jar = f"{upper_name}{new_name}"
name_jar = f"fullname: {upper_name}{lower_name}{name}" # \t, \n, \r
print(name)
print(new_name)
print(upper_name)
print(lower_name)
print(name_jar)

word_num = "first"
word = "        hello world       "
word_last = "last"

#left_word = word.lstrip()
#left_word = left_word.rstrip()
left_word = word.strip()
new_word = f"{word_num}{left_word}{word_last}"
print(new_word)

car_name = "mercedez benz"
adjective_car = f"A beautiful {car_name}"
another_name = f"{upper_name}: ggshshsj: {car_name}"
space_no_name = " "
print(space_no_name)
print(type(space_no_name)) # use function type() to get the data type of any variable
no_name = space_no_name.strip()
print(no_name)
print(type(no_name))




