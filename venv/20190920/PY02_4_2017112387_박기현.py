inp, num, ten, one, tmp, cnt= 0, 0, 0, 0, 0, 1

inp = int(input("0 ~ 99 사이 숫자 입력 : "))

num = inp
while True:
    ten = num // 10
    one = num % 10

    tmp = ten + one

    num = one*10 + tmp%10

    print("%d 번째 숫자: %d" % (cnt, num))

    if num == inp:
        break
    else:
        cnt = cnt + 1

print("최종 연산 횟수 : %d 번" % cnt)