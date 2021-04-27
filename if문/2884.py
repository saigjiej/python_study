# 2884번 : 알람 시계
hour, minute = map(int, input().split())

if minute > 44:  # 분이 45분 이상일 경우
    print(hour, minute-45)
elif minute < 45 and hour > 0:  # 분이 44분 이하이고 시간이 1시 이상일 경우
    print(hour-1, (minute-45)+60)  #  분이 44분 이하일 경우 45분을 뺐을 경우 음수가 나오기 때문에 양수가 나올 수 있도록 60을 더해주고 hour-1을 해줍니다.
else:  # hour이 음수일 경우
    print(23, (minute-45)+60)