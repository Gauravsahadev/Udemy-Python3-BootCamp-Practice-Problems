# Program to check wheather names end with a or not
lst = []
names = input("Enter the names: ").split()
[lst.append(names[i]) for i in range(len(names))]
last_a = list(filter(lambda x: x[-1] == "a", lst))
print(last_a)
