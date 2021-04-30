# 2438번 : 별 찍기 - 1
a = int(input())
for i in range(a):
    print("*" * (i+1))  # 0부터 시작하기 때문에 1을 더하여 입력한 수만큼 출력할 수 있도록 함