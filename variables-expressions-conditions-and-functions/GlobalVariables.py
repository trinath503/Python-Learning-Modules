# This function has a variable with
# name same as s.

s = 1
def f():
    global s
    print(s)
    s = "Me too."
    print(s)


s = "I love Geeksforgeeks"
f()
print("Welcome",s,"Nice to see you", s)
