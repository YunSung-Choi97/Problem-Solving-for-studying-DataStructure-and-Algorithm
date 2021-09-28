import sys
input = sys.stdin.readline

def fibonacci(n):  # n번째 피보나치 수를 리턴하는 함수
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

n = int(input())

print(fibonacci(n))