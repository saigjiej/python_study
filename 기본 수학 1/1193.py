# 1193번 : 분수찾기
num = int(input())  # 몇 번째 분수를 구할 것인지 입력

line = 0
max_num = 0

while num > max_num:
    line += 1
    max_num += line

gap = max_num - num

if line % 2 == 0:  # line이 짝수일 경우
    top = line - gap
    under = gap + 1
else:  # line이 홀수일 경우
    top = gap + 1
    under = line - gap
print(top, '/', under)