# A simple program to do math calculations
def add(num1, num2):
    pass
    return num1+num2


def subtract(num1, num2):
    pass
    return num1-num2


def multiply(num1, num2):
    pass
    return num2*num1


def divide(num1, num2):
    pass
    return num1/num2


def math(num1, num2, fn=add):
    return fn(num1, num2)


lst = []
num = input("Enter the numbers and operation: ").split()
[lst.append(num[i]) for i in range(len(num))]

print(math(int(lst[0]), int(lst[1]), add))
