#10809번 : 알파벳 찾기
word = input()
alphabet = list(range(97, 123))

for x in alphabet:
    print(word.find(chr(x)))  # chr() - 아스키 코드 값을 문자로 변환해 주는 함수