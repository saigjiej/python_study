# 1330번 : 두 수 비교하기
# split 함수를 이용하여 공백을 기준으로 문자를 나눈 후 map 함수를 사용해서
# split 함수로 나눈 두 개의 문자를 int 타입으로 변환
A, B = map(int, input().split())
if A > B:  # A가 B보다 클 경우
    print(">")
elif A < B:  # A가 B보다 작을 경우
    print("<")
else :  # 그 이외, A와 B가 같을 경우
    print("==")