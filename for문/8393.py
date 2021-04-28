# 8393번 : 합
n = int(input())
sum = 0  # 1부터 n까지의 합 저장 변수
for i in range(1, n+1): # 1부터 n까지 반복
    sum += i  # sum에 1부터 n까지의 합 저장
print(sum)