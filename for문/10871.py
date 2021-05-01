# 10871번 : X보다 작은 수
cnt, X = map(int, input().split()) # split() 함수를 이용해서 공백을 기준으로 a, b에 저장하고 map()함수로 int형 변환
B = list(map(int, input().split()))  # X보다 작은 수를 구별하기 위한 수 작성 시 공백 기준으로 나누어 리스트에 저장 후 int형으로 변환
for i in range(cnt): # 입력한 수만큼 반복
    if B[i] < X: # 만약 X보다 작은 수일 경우
        print(B[i]) # 작은 수 출력