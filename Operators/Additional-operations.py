# / division to return float result
print(5/2)
print(-5/2)
# // division to return int result
print(5//2)
print(-5//2)

# Python code to demonstrate working of
# add(), sub(), mul()

# importing operator module
import operator

# Initializing variables
a = 4

b = 3

# using add() to add two numbers
print("The addition of numbers is :", end="");
print(operator.add(a, b))

# using sub() to subtract two numbers
print("The difference of numbers is :", end="");
print(operator.sub(a,b))

# using mul() to multiply two numbers
print("The product of numbers is :", end="");
print(operator.mul(a, b))

if a.isdigit():
    print(a)