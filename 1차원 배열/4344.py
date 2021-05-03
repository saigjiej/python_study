# 4344번 : 평균은 넘겠지
n = int(input())  # 몇 번의 점수를 입력할 것인지 개수 입력

for _ in range(n):
    # split() 함수를 사용하여 입력 받은 값을 공백 기준으로 number에 저장 후 map() 함수를 이용하여 int로 변환
    number = list(map(int, input().split()))
    # number[0]은 학생 수, number[1: ]은 학생의 점수가 저장되어 있으므로 슬라이싱을 이용하여 평균을 구함
    avg = sum(number[1:]) / number[0]
    count = 0
    for score in number[1:]:  # 입력한 점수의 수만큼 반복
        if score > avg:  # 만약 입력한 점수가 평균보다 높다면
            count += 1   # count가 1씩 증가
    rate = count / number[0] * 100   # 평균보다 높은 학생 비율 구하기
    print(f'{rate:.3f}%')  # f-string으로 소수점 셋째 자리까지 출력