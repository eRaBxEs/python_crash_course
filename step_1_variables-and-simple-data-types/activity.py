trinity_1 = "God the Father"
trinity_2 = "God the Son"
trinity_3 = "God the Holy Spirit"

#  Activity 1. Create a variable called trinity that combines the 3 variable above as a string 
#  using the new formatting string technique which exist in python 3.6 and above

trinity = f"{trinity_1}: GOD,\n{trinity_2}: Jesus, \n{trinity_3}: Holy Ghost. \nThese make up the trinity"
print(trinity)

#  Activity 2. Create a variable called trinity that combines the 3 variable above as a string 
#  using the old formatting string technique which exist in python 3.5 and below

trinity_other = "{}: GOD\n{}: Jesus\n{}: Holy Ghost. \nThese make up the trinity".format(trinity_1,trinity_2,trinity_3)
print(trinity_other)
