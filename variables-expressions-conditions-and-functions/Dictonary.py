tri = {'Name':'Trinath','Age':'20','ID':'101','Passion':'Coding'}

# print only the keys
print(tri.keys())

# print only values

# for item in tri.values():
#     print(item)
print(tri.values())

#find key is there or not
t =tri.has_key('Age')
print(t)

# using str() to display dic as string
print ("The constituents of dictionary as string are : ",str(tri))

# using len() to display dic size
print ("The size of dic is : ",len(tri))

# using type() to display data type
print ("The data type of dic is : ",type(tri))


# using copy() to make shallow copy of dictionary
dic3 = tri.copy()

# clearing the dictionary
dic3.clear()