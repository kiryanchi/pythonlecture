aa = []
sum = 0

# lengths before making list
print("생성 전 길이 => %d" % len(aa))

for i in range(0,100,1):
    aa.append(i)
    sum += aa[i]


# lengts after appending list
print("추가 후 길이 => %d" % len(aa))

print("합계 : %d" % sum)