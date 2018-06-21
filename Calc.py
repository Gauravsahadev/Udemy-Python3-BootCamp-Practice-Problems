x=int(input("Enter the first number "))
y=int(input("Enter second number "))
op=   input("Enter operator 1.Add 2.Subs 3.Mult 4.Divide")
if(op==1):
	print(x+y)
elif(op==2):
	print(x-y)
elif(op==3):
	print(x*y)
elif(op==4):
	print(x/y)
else:
	print("Wrong Choice")
