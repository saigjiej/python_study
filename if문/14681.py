# 14681번 : 사분면 고르기
q1 = int(input())
q2 = int(input())

# and는 두 값이 모두 True여야 True
# or는 두 값 중 하나라고 True이면 True
if q1 > 0 and q2 > 0:  # q1이 0보다 크고 q2가 0보다 클 경우
    print("1")
elif q1 < 0 and q2 > 0:  # q1이 0보다 작고 q2가 0보다 클 경우
    print("2")
elif q1 < 0 and q2 < 0:  # q1이 0보다 작고 q2가 0보다 작을 경우
    print("3")
else:  # 나머지
    print("4")