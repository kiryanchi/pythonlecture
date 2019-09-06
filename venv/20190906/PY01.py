
# input() 은 String 으로 받아옴 int 로 캐스팅해저야함
#print("숫자를 입력하세요")
a = int(input("숫자 1 입력하세요 : "))
b = int(input('숫자 2 입력하세요 : '))

result = a + b
print(a, "+", b, "=", result)

result = a - b
print(a, "-", b, "=", result)

result = a * b
print(a, "*", b, "=", result)

result = a / b
print(a, "/", b, "=", result)


#{인덱스번호}
print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))

print("I eat {} {} {} apples".format("five", 3, "one"))

print("I eat {n} apples".format(n=9))

# % 떼고 써야함. d 만 쓰면됨
print("{0:d} {1:5d} {2:05d}".format(123, 234, 345))

"""
이렇게 뜬다.

>>> '{:>5}'.format(123)
'  123'
>>> '{:>10}'.format(123)
'       123'
>>> '{:>05}'.format(123)
'00123'

"""
