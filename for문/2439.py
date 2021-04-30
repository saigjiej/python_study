# 2439번 : 별 찍기 - 2
N = int(input())
for i in range(1, N+1): # 1부터 N까지 반복
    print(" " * (N-i) + "*" * i)  # i가 1부터 시작하므로 N-i씩 공백을 곱해주고, *을 i씩 곱해 더하여 출력