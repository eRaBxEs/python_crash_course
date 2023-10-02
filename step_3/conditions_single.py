# Testing for a single condition
age = 12

if age < 4 :
	pay = 0 
elif age < 18 :
	pay = 20
elif age < 65 :
	pay = 35
elif age >= 65 :
	pay = 20

print(f"you are to pay {pay}")