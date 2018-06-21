# Simple program to raise power of any number
# If no power input is given it squares the number


def exponent(num, power=2):
    pass
    return num**power


lst = []
num = input("Enter the number and the power to raise: ").split()
[lst.append(num[i]) for i in range(2)]
print(exponent(int(num[0]), int(num[1])))
