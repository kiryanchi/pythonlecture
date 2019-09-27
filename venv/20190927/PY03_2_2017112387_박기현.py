a = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta"]
output = []

length = int(input("문자열 길이: "))

for i in range(0, len(a), 1):
    if ( len(a[i]) == length ):
        output.append(a[i])

print(output)