# 1065번 : 한수
n = int(input()) # 범위 입력
han = 0

for i in range(1, n + 1): # 1부터 입력한 범위까지 반복
    if i < 100: # 만약 i가 100보다 작을 경우 (1부터 99까지는 모두 한수이다)
        han += 1 # 1을 증가
    else: # 100이거나 100보다 클 경우
        ns = list(map(int, str(i)))  # map()을 이용하여 i를 문자열로 변환 후 리스트에 저장하고 정수형으로 변환(숫자를 자릿수대로 분리)
        if ns[0] - ns[1] == ns[1] - ns[2]: # 만약 첫 번째 숫자 - 두 번째 숫자와 두 번째 숫자 - 마지막 숫자의 값이 같을 경우 등차수열이다
            han += 1 # 1을 증가
print(han) # 한수 출력