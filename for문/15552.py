# 15552번 : 빠른 A+B
import sys

inp = int(input())
for i in range(inp):  # inp-1만큼 반복
    # 사용자로부터 입력을 최대한 빠르게 받아야하는 경우
    # sys 라이브러리가 저장되어 있는 sys.stdin.readline() 메서드 이용
    a, b = map(int, sys.stdin.readline().split())  # split() 함수를 사용하여 입력 받은 값을 공백 기준으로 a, b에 저장 후 map() 함수를 이용하여 int로 변환
    print(a + b)