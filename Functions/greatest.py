# Simple Program to check the greatest number
def greatest(a, b):
    pass
    if a > b:
        print("{} is greater. ".format(a))
    elif b > a:
        print("{} is greater.".format(b))
    else:
        print("{} and {} are equal!".format(a, b))


num_list = []
num = input("Enter the numbers:").split()
[num_list.append(num[i]) for i in range(len(num))]
greatest(int(num_list[0]), int(num_list[1]))
