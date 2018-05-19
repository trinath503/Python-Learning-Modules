# Python code to demonstrate Type conversion

# initializing string
s = "100"


print("Convertion of string to Int: ", int(s))

print("Convertion of string to Float: ", float(s))

print("Convertion of Character to Float: ", ord("A"))

print("Convertion of Number to Hex: ", hex(21))

print("Convertion of Number to Oct: ", oct(21))

print("Convertion of String to Tuple: ", tuple("Trinath Reddy")) #you can print the truple as list in loop as

print("Convertion of String to set: ", set("Trinath Reddy"))


# printing integer converting to complex number
c = complex(1, 2)
print("After converting integer to complex number : ",c, end="")

print()
# printing integer converting to string
print("After converting integer to string : ", str(20), end="")
print()

#list creation
tri= ['5','3','4','2']
#list deletion
del tri[2]
#list appending
tri.append('5')
#list reverse
tri.sort(reverse=True)
print(tri)


#tuple creation
tup = (('a', 1) ,('f', 2), ('g', 3))
# dictionary creation or tuple to dictionary convertion
dictionary =dict(tup)
#deletion of dictionary
del dictionary['a']
print("Convertion of String to Dictionary: ", dictionary.keys())


