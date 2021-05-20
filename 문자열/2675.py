# 2675번 : 문자열 반복
t = int(input()) # 문자열을 몇 개 입력할 것인지 입력
for i in range(t): # 문자열을 입력한 개수만큼 반복
    num, s = input().split() # 문자열을 몇 번 반복한 것인지와 문자열 s 입력
    text = "" # 문자열로 초기화(문자열 반복을 위해)
    for i in s: # 입력한 문자열만큼 반복
        text += int(num) * i # 개수 * 문자열
    print(text) # 문자열 반복한 것 출력