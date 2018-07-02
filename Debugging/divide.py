#Program to divide by try and except

def divide(a,b):
	pass
	try:
		result=a/b
	except (ZeroDivisionError,TypeError) as err:
		print("Something went wrong!")
		print(err)
	else:
		pass
		print("The result is {}".format(result))

divide(3,4)
