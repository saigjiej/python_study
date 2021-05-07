# 11720번 : 숫자의 합
a = int(input())
b = list(input())
result = 0

for i in b:  # 입력받은 리스트만큼 반복
    result += int(i)  # 입력받은 리스트는 문자열이기 때문에 int형으로 변환하여 모든 합을 구함
print(result)  # 합 출력