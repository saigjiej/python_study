# 10950번 : A+B - 3
count = int(input()) # 몇 번 입력할지 count 입력
for i in range(count): # count-1만큼 반복
    # 입력받은 후 split() 함수로 공백을 기준으로 하여 a, b에 저장
    # map() 함수를 사용하여 문자열을 정수로 변환
    a, b = map(int, input().split())
    print(a + b)