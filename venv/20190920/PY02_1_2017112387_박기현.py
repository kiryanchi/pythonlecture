money = int(input("교환할 돈은 얼마? "))

change = money // 500
money %= 500

print("500원짜리 : %d 개" % change)

change = money // 100
money %= 100

print("100원짜리 : %d 개" % change)

change = money // 50
money %= 50

print("50원짜리 : %d 개" % change)

change = money // 10
money %= 10

print("10원짜리 : %d 개" % change)
print("바꾸지 못 한 잔돈 : %d 원" % money)