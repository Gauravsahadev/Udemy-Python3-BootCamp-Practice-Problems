# Program to sum up all given number using *args or *
def sum_up(*nums):
    total = 0
    for num in nums:
        total += int(num)
    return total


# Input number in list by user
lst=[]
number=input("Enter numbers: ").split()

[lst.append(number[i]) for i in range(len(number))]
print(lst)
print("sum=",sum_up(*lst))

