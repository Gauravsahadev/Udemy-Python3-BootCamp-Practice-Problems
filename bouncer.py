#Input the age
age =input("Enter your age: ")
#Check for truthiness
if age:
	#Type conversion from str=>int
	age=int(age)
	#Check if age greater than or equal to 21 and print result
	if age>=21:
		print("You can enter and drink!")
	#Check if age greater than or equal to 18 and print result	
	elif age>=18:
		print("You can enter but need wristband!")
	#print if too young!
	else:
		print("Sorry,little one! :(")
#If wrong input enter.
else:
	print("Please Enter something!")