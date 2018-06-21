#First method
for num in range(1,21):
	if num==4 or num==13:
		print("{} is Unlucky".format(num))
	elif num%2==0:
		print("{} is even".format(num))
	else:
		print("{} is odd".format(num))
#Second Method
for num in range(1,21):
	if num==4 or num==13:
		state="Unlucky"
	elif num%2==0:
		state="even"
	else:
		state="odd"
	print("{} is {}".format(num,state))