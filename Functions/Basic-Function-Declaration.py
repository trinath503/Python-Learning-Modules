# A Python program to demonstrate that a function
# can be defined inside another function and a
# function can be passed as parameter.

# Adds a welcome message to the string
def messageWithWelcome(str):
    # Nested function
    def addWelcome():
        return "Welcome to "

    # Return concatenation of addWelcome()
    # and str.
    return addWelcome() + str
# --------------------------------------------------------------- #

# To get site name to which welcome is added
def site(site_name):
    return site_name


print(messageWithWelcome(site("GeeksforGeeks")))


# Correct way of writing empty function
# in Python
def fun():

    pass
    print('hi')
fun()

# --------------------------------------------------------------- #