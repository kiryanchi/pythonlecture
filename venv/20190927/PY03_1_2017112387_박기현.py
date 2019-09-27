a = []
b = []
c = []

for i in range(0,4,1):
    a.append(i+1)
    b.append(i+5)
    c.append(i+9)

list_2 = [a,b,c]

for i in [0,1,2]:
    print("list_1(%d): " % i, list_2[i])

print("-----------------------------------------------------------")

print("list_2: ", list_2)

print("-----------------------------------------------------------")

for i in range(0,len(list_2),1):
    for j in range(0,len(list_2[0]),1):
        print("list_2[%d][%d] :" %(i,j), "%-4d" % list_2[i][j], end="")
    print()