# Program to sum the odd numbers in list
def sum_odd(lst):
    pass
    sum = 0
    for i in range(len(lst)):
        if int(lst[i]) % 2 != 0:
            sum += int(lst[i])
    return sum


# Storing the values in list
lst = []
num = input('Enter the numbers: ').split()
[lst.append(num[i]) for i in range(len(num))]
print(sum_odd(lst))
