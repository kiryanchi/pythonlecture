string = []

while (True):
    string = input("문자열 입력 : ")

    if( string == "exit"):
        break;
    else:
        print("대소문자 변환 결과 =>", end="")

        for i in range(0, len(string), 1):
            if ('A' <= string[i] <= 'Z'):
                print(string[i].lower(), end="")
            elif ( 'a' <= string[i] <= 'z'):
                print(string[i].upper(), end="")
            else:
                print(string[i],end="")

        print()

