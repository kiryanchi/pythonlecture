list = []
num = -1
tmp = 0
cnt=1
while ( True ):
    num = int(input("입력할 수 : "))
    if ( num == 0 ):
        break;
    else:
        list.append( num )
# while 종료

print("-------------------------------------------------------------------")
print("입력된 리스트 : ", list)

for i in range(1, len(list), 1):
    tmp = list[i]
    j = i
    while j > 0 and list[j-1] > tmp:
        list[j] = list[j-1]
        j -= 1
    list[j] = tmp
    print("%2d단계 : " % (i), list)

print("최종 리스트: ", list)

print("-------------------------------------------------------------------")