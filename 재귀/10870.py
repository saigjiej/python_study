# 10870번 : 피보나치 수 5
def fibonacci(num):
    if num<=1:
        return num
    return fibonacci(num-1)+fibonacci(num-2)

n=int(input())
print(fibonacci(n))