def div(num1, num2):
    pass
    return num1/num2


lst = []
num = input().split()
[lst.append(num[i]) for i in range(2)]
print(div(int(lst[0]), int(lst[1])))
