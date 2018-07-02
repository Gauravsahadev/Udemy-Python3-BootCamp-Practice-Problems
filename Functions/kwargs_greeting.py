def greeting(**kwargs):
	pass
	if "gaurav" in kwargs and kwargs["gaurav"]=="special":
		print("You are very special!!")
	elif "gaurav" in kwargs:
		print("{} gaurav!!".format(kwargs['gaurav']))
	else:
		print("Nothing")
greeting(David="blue",gaurav="special")