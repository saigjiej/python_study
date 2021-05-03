# 2562번 : 최댓값
a = []  # 리스트 초기화
for i in range(9):  # 9번 반복
    a.append(int(input()))  # 9개의 서로 다른 자연수 입력
print(max(a))  # max()을 이용하여 a 중 최댓값 찾기
print(a.index(max(a)) + 1)  # index()을 이용하여 최댓값이 몇 번째 수인지를 구하고 인덱스가 0부터 시작하여 1씩 적기에 1을 더하여 원래의 인덱스를 구함
