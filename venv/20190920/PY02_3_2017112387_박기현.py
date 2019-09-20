a, b = 0, 0

for b in range (1,10,1) :
    for a in range (2,10,1) :
        print("%dx%d=%2d  " % (a, b, a*b), end="")
    print(" ")