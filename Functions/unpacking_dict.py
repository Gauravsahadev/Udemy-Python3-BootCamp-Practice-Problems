# Program to unpack dictionary and pass to the function.


def unpack(a, b, c):
    pass
    print(a+b*c)


data = dict(a=2, b=4, c=6)
data2 = {"a": 3, "b": 5, "c": 7}
unpack(**data)
unpack(**data2)
