# 1157번 : 단어 공부
words = input().upper() # 단어 입력
unique_words = list(set(words)) # 입력한 단어를 list로 저장(중복 X)

cnt_list = [] # 리스트 초기화
for x in unique_words : # 입력한 단어만큼 반복
    cnt = words.count(x) # 입력한 단어의 알파벳을 입력한 단어와 비교하며 개수를 셈
    cnt_list.append(cnt) # 사용된 알파벳의 개수를 저장

if cnt_list.count(max(cnt_list)) > 1 : # 만약 가장 많이 사용된 알파벳이 여러 개일 경우
    print('?') # ? 출력
else : # 아닐 경우
    # cnt_list에서 가장 많이 사용된 알파벳의 인덱스를 max_index에 저장
    max_index = cnt_list.index(max(cnt_list))
    print(unique_words[max_index]) # 가장 많이 사용된 알파벳의 인덱스 값을 출력