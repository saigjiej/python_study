# 8958번 : OX퀴즈
a = int(input())  # 몇 개를 입력할 것인지 입력
for i in range(a):  # 입력한 만큼 반복
    b = input()  # 점수 입력
    s = list(b)  # 입력한 점수를 s에 list로 저장
    sum = 0
    c = 1
    for i in s:  # 입력한 점수의 list 요소 반복
        if i == 'O':  # 만약 i가 O라면
            sum += c  # c를 더하고
            c += 1  # c을 1씩 더함 (O가 연속됐을 경우, 1씩 더 더함)
        else:  # 만약 i가 O가 아니라면
            c = 1
    print(sum) # 구한 점수를 출력