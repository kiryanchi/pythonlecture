# Hello World!
print("hello world!")

"""
주석을
이렇게
달면됨
"""

print("hello", "world")
print("1" , "2" , "3")

#문자 일영영
print("100")

#숫자 100
print(100)

# , 가 아니라 % 로 구분함
print("%d" % 100)

# 문자
print("100 + 100")

#숫자
print(100+100)
print("%d" % (100+100))

#에러
# print("%d" % (100, 100))

#반드시 괄호를 써ㅓ줘야함!!
print("%d %d" % (100, 200))

# 0.5 를 %d 로 하면 0으로 나옴. %f 로 해야함
print("%d %d %f" % (100, 200, 0.5))

# %g 는 자기가 알아서 해줌
print("%g" % 1.234)

print('%(language)s has %(number)03d quote types.' % {'language': "Python", "number" : 2})

print('python programming')

print("What's your name")

print(""" Characters of name?
    1. platform independent
    2. interpreter
    3. object=oriented programming
    """)

# ' 와 " 는 별개로 침

print(' 이렇게 "별개"로 됨')
print(" 이렇게도 '별개'로 ")

print(r"\n \t \" \\ 을 그대로 출력")