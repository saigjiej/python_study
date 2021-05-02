# 1110번 : 더하기 사이클
num = int(input())  # 주어진 수
check = num  # check에 num을 저장
temp = 0
new_num = 0
count = 0
while True:
    temp = (num // 10) + (num % 10) # num // 10을 하여 십의 자리, num % 10을 하여 일의 자리를 구하여 더함
    # num % 10을 하여 주어진 수의 가장 오른쪽 자리 수를 구하고 10을 곱하여(이어붙여야 하기 때문) 2자리 수를 만들고 temp % 10을 하여 구한 합의 오른쪽 자리 수를 구함
    # 그리고 주어진 수의 오른쪽 자리 수를 2자리 수로 변환한 것과 구한 합의 오른쪽 자리 수를 더하여 이어붙임
    new_num = (num % 10) * 10 + (temp % 10)
    count += 1  # 원래 수로 돌아오기 위한 num의 사이클의 길이 구하기 위하여 1씩 더해줌
    num = new_num  # num을 new_num으로 저장
    if new_num == check:  # new_num(새로 만든 문자)와 check(입력 받은 수)가 같을 경우
        break  # while문 빠져나옴
print(count)  # num의 사이클의 길이 출력