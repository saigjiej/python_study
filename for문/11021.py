# 11021번 : A+B - 7
A = int(input())
for i in range(A):
    # split() 함수를 사용하여 공백을 기준으로 A, B에 저장하고 map() 함수를 사용하여 int형으로 변환한다.
    A, B = map(int, input().split())
    # 문자열로 출력을 위해서 str() 함수를 사용하고 i는 0부터 시작하기에 1을 더하여 1부터 시작하게 출력한다.
    print("Case #" + str(i+1) + ":", A+B)