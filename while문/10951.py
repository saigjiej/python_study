# 10951번 : A+B - 4
# try - except 구문 활용
while True:  # True일 경우 계속 반복
    try:  # 에러가 발생할 여지가 있는 문장
        a, b = map(int, input().split())
        print(a + b)  # 에러가 발생하지 않는 경우 a + b 값 출력
    except:  # 에러 발생 시 실행 시킬 문장
        break  # whlie문 빠져나옴