def colorize(text,color):
	pass
	colors=("red","blue","green","black","cyan")
	if type(text) is not str:
		raise TypeError("Text must be a instance of string")
	if color not in colors:
		raise NameError("color is not present")

	print("The {} is {} colour".format(text,color))

colorize("hello","red")