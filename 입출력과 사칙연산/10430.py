# 10430번 : 나머지
A, B, C = input().split()  # input() 함수를 사용하여 A, B, C를 입력받은 후 split() 함수를 사용하여 세 수인 A, B, C를 나누어서 저장
# A, B, C = map(int, input().split()) => map() 함수를 이용하여 int 변환과 한 줄로 작성 가능
A = int(A)  # int() 함수를 사용하여 정수로 변환
B = int(B)
C = int(C)
print((A+B)%C)
print((A%C + B%C)%C)
print((A*B)%C)
print((A%C * B%C)%C)
# print(A+B, A-B, A*B, A//B, A%B, sep='\n')	=> sep='\n'로 줄바꿈