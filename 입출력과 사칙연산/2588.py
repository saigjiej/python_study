# 2588번 : 곱셈
A = int(input())  # input() 함수는 숫자를 입력해도 문자열로 입력되므로 int()를 사용하여 정수로 변환
B = input()  # 입력받은 숫자를 하나씩 떼어내야하기 때문에 정수로 바꾸지 않고 그대로 둠

# 문자열의 인덱스를 이용하여 뒤에서부터 A와 곱함
num1 = A * int(B[2])
num2 = A * int(B[1])
num3 = A * int(B[0])
num4 = A * int(B)  # int()를 사용하여 정수를 바꾸지 않을 경우 오류

print(num1)
print(num2)
print(num3)
print(num4)