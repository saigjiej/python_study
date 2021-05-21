# 1152번 : 단어의 개수
string = input("") # 문자열 입력받기
words = string.split(" ") # 입력받은 문자열을 공백 제거
words = [i for i in words if i != ""] # 공백이 아닌 경우에만 words에 저장
print(len(words)) # 몇 개의 단어가 있는지 알기 위해 길이 출력