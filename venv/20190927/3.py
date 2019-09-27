ss = input("문자열 입력: ")

print("출력 문자열 => ", end="")

for i in range(0, len(ss), 1):
    if ss[i] == 's':
        print("$", end="")
    else:
        print(ss[i], end="")