m = [[1,2],[3,4],[5,6]]
tri = [ [m[j][i] for j in range(len(m))]for i in range(len(m[0]))]


# tri = [ [m[j][i] for j in range(len(m)) if m[j][i]!=5 and m[j][i]!=2]for i in range(len(m[0]))]
#

print(tri)