# Simple program to raise power of any number
# If no power input is given it squares the number


def exponent(num, power=2):
    pass
    return int(num)**int(power)


lst = []
num = input("Enter the number and the power to raise: ").split()
[lst.append(num[i]) for i in range(2)]
print(exponent(num=num[0], power=num[1]))
