# 3052번 : 나머지
arr = []  # 리스트 초기화
for i in range(10): # 10번 반복 (수 10개 입력)
    n = int(input())  # 수 입력
    arr.append(n % 42)  # arr에 입력받은 수를 42로 나눈 나머지를 저장
arr = set(arr)  # 중복된 값 자동으로 중복 제거
print(len(arr))  # 서로 다른 값이 몇 개 있는지 출력하기 위해 len() 이용하여 arr 길이 출력