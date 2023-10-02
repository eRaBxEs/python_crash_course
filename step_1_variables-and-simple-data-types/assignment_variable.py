# Variables can be described as boxes/containers, 
# but an accurate way to describe a variable is that variables are lables that you can assign to values
# or that variables references a certain value
tool_name = "screw-driver"

# multiple assignment :: numbers : comment
x, y, z = 4, 6, 8
print(x, y, z)


# multiple assignment :: strings
name_boy, name_girl, name_baby = "Jack", "Jane", "Dolly"
print(name_boy)
print(name_girl)
print(name_baby)
name_boy = "Jackie Chan"
name_girl = "Jane Chan"
name_baby = "Dolly Chan"
print(name_boy)
print(name_girl)
print(name_baby)

# constant Pie is declared here
PIE = 3.1468
radius = 28

area_circle = PIE * radius * radius
print("The area of the circle: ", area_circle)
