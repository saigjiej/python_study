# 15596번 : 정수 N개의 합
def solve(n):  # n를 입력받는 함수
    ans = 0
    ans += sum(n)  # sum() 사용해서 합을 구함
    return ans  # 정수 n개의 합을 구한 것을 반환