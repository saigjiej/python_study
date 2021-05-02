# 10952번 : A+B - 5
# whlie은 어떤 조건이 만족되는 동안 그 아래에 쓴 문장들을 반복하는 기능을 갖고 있음
while True: # True일 경우 계속 반복
    a, b = map(int, input().split())  # split()으로 입력받은 값을 공백을 기준으로 나누어 a, b에 대입 후 map()으로 int형 변환
    if a == 0 and b == 0:  # a와 b가 0일 경우
        break  # True문을 빠져나옴
    print(a + b)  # a와 b가 0이 아닐 경우 a + b 값 출력
