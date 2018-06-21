age=input("Enter the age: ")

if not ((age>="2" and age<="12") or age>="65"):
	print("10 dollar per ticket!")
elif age>="2" and age<="12":
	print("2 dollar per ticket!")
elif age>="65":
	print("5 dollar per ticket!")
