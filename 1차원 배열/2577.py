# 2577번 : 숫자의 개수
a = int(input())
b = int(input())
c = int(input())

k = a*b*c  # 입력받은 세 수를 곱함
k_list = list(str(k))  # 곱한 세 수를 문자열로 리스트에 저장
for i in range(10): # 0부터 9까지 반복
    count_list = k_list.count(str(i))  # 리스트 중 0부터 9까지 사용한 개수를 문자열로 count_list에 저장
    print(count_list)  # 0부터 9까지 중 사용한 개수 출력
