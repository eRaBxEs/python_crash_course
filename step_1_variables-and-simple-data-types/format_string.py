first_name = "ada"
last_name =  "lovelace"
full_name = f"{first_name} {last_name}" # using new format style of python 3.6 and above
message = f"Hello, {full_name.title()}"
print(message)

all_names = "{} {}".format(first_name, last_name)
new_message = "Hello, {}".format(all_names.title())
print(new_message)