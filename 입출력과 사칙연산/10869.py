# 10869번 : 사칙연산
A, B = input().split()  # input() 함수를 사용하여 A, B을 입력받은 후 split() 함수를 사용하여 두 수를 A, B로 나누어 저장
# A, B = map(int, input().split()) => map() 함수를 이용하여 int 변환과 한 줄로 작성 가능
A = int(A)  # int() 함수를 사용하여 정수로 변환, int() 사용하지 않을 시 오류발생
B = int(B)
print(A + B)
print(A - B)
print(A * B)
print(A / B)  # print(A / B)일 경우 소수로 출력 됨
print(A % B)