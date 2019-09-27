price = []

price = list(map(int, input("가격을 입력하세요: ").split(';')))


# 오름차순 정
price.sort(reverse=True)
#    print(price[i].format(3,','), end="")

for i in range(0, len(price), 1):
    print("%9s" % format(price[i],',') )