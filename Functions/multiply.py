# Program to multiply any two number

# Function to multiply


def multiply(num1, num2):
    pass
    return num1*num2


# storing the values in list
lst = []
print("Enter the two numbers: ")
num = input().split()
[lst.append(num[i]) for i in range(2)]
print(multiply(int(lst[0]), int(lst[1])))
