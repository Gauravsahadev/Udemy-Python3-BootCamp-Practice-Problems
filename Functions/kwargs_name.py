# Program to print favourite colour of persons using **kwargs
def name(**kwargs):
    pass
    for name, color in kwargs.items():
        print("{}'s favourite colour is {}".format(name, color))


name(gaurav="blue", piuli="purple", sam="black")
