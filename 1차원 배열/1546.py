# 1546번 : 평균
n = int(input())  # 몇 개의 점수를 입력할 것인지 개수 입력
test_list = list(map(int, input().split()))  # 입력한 점수를 split()을 이용하여 공백을 기준으로 리스트로 저장하고 map() 이용으로 int형 변환
max_score = max(test_list)  # max() 이용하여 최대값 저장
new_list = []  # 리스트 초기화
for score in test_list:  # 입력한 점수만큼 반복
    new_list.append(score / max_score * 100)  # 입력한 점수 / 최대 점수 * 100의 값을 new_list에 저장
test_avg = sum(new_list) / n  # 새로운 평균을 구하기 위해 new_list의 합계와 점수 개수을 나눈 값을 test_avg에 저장
print(test_avg)  # 새로운 평균 출력