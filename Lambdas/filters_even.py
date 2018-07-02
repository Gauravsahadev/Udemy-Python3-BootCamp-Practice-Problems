# Filter example

l = []
num = input("Enter number: ").split()
[l.append(int(num[i])) for i in range(len(num))]
evens = list(filter(lambda x: x % 2 == 0, l))
print(evens)
