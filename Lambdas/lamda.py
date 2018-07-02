#Program to add and square number using lambda

square=lambda num:num*num
add=lambda a,b:a+b
print(square(9),add(5,6))

print(square.__name__)
print(add.__name__)