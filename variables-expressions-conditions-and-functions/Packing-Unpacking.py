def upPacking(*unpack_list):
    for item in range(len(unpack_list)):
        print(unpack_list[item])


unpack_list = ['1','2','3','4']
upPacking(*unpack_list)


# A Python program to demonstrate use
# of packing

# This function uses packing to sum
# unknown number of arguments
def mySum(*args):
    sum = 0
    for i in range(0, len(args)):
        sum = sum + args[i]
    return sum


# Driver code
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))

#unpacking
# A sample function that takes 4 arguments
# and prints the,
def fun(a, b, c, d):
    print(a, b, c, d)


# Driver Code
my_list = [1, 2, 3, 4]

# Unpacking list into four arguments
fun(*my_list)