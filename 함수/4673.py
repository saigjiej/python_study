# 4673번 : 셀프 넘버
numbers = set(range(1, 10000)) # 10000보다 작거나 같은 범위이므로 set()과 range()을 이용하여 1부터 10000까지 범위 설정
numbers_set = set() # set() 함수 -> 집합으로 중복을 없앰
for num in numbers: # 1부터 10000까지 반복
    for n in str(num): # num을 str()을 이용하여 문자열로 변환 후 반복(75일 경우 7, 5처럼 하나씩 떼어내기 위해)
        num += int(n) # n을 int()을 이용하여 정수로 변환 후 더함(75일 경우 75+7+5의 값을 저장)
    numbers_set.add(num) # numbers_set에 자리 수를 분리하여 더한값을 add()을 이용하여 저장함

self_number = numbers - numbers_set # 생성자가 없는 숫자인 셀프넘버를 구하기 위해 1부터 10000까지와 생성자로 생겨난 수를 빼어 구함
for self_num in sorted(self_number): # self_numbers를 오름차순으로 정렬함
    print(self_num) # 셀프넘버 출력