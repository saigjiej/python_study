# 9498번 : 시험 성적
score = int(input()) # 입력받은 score(시험점수)를 정수로 변환
if 100 >= score and 90 <= score:  # 90 <= score <= 100
    print("A")
elif 89 >= score and 80 <= score:  # 80 <= score <= 89
    print("B")
elif 79 >= score and 70 <= score:  # 70 <= score <= 79
    print("C")
elif 69 >= score and 60 <= score:  # 60 <= score <= 69
    print("D")
else:  # 나머지
    print("F")