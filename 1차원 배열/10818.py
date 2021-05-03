# 10818번 : 최소, 최대
numbers = int(input())  # 몇 개의 정수를 입력할 것인지 입력
number_list = list(map(int, input().split()))  # N개의 정수 입력

max_num = number_list[0]  # max_num(최대값)을 입력받은 리스트의 첫번째 값으로 초기화
min_num = number_list[0]  # min_num(최소값)을 입력받은 리스트의 첫번째 값으로 초기화
for num in number_list:  # 입력받은 리스트만큼 반복
    if num > max_num:  # 입력받은 리스트 값끼리 비교를 하여 더 큰 값일 경우
        max_num = num   # max_num에 저장
    if num < min_num:  # 입력받은 리스트 값끼리 비교를 하여 더 작은 값일 경우
        min_num = num  # min_num에 저장
print(min_num, max_num)  # 최소값과 최대값 출력