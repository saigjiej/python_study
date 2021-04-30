# 11022번 : A+B - 8
count = int(input())  # 몇 번 입력할 것인지 count 입력
for i in range(count):  # count만큼 반복
    # split() 함수를 사용하여 공백을 기준으로 A, B에 저장하고 map() 함수를 사용하여 int형으로 변환한다.
    A, B = map(int, input().split())
    print("Case #%d: %d + %d = %d" %(i+1, A, B, A+B))