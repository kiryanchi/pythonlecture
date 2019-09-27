aa = []
bb = []
num = 0

for i in range(0,200,2):
    aa.append(i)

num = len(aa)

for i in range(num-1,-1,-1):
    bb.append(aa[i])

print("aa[0]: %d ~ aa[%d]: %d" %(aa[0], num-1, aa[num-1]))
print("bb[0]: %d ~ bb[%d]: %d" %(bb[0],i,bb[i]))