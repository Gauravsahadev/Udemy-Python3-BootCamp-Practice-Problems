# Program to sum up all given number using *args or *
def sum_up(*nums):
    total = 0
    for num in nums:
        total += num
    return total


# Input number in list by user
print(sum_up(1, 2, 3, 4, 5, 6, 7))
print(sum_up(3, 6, 7))
