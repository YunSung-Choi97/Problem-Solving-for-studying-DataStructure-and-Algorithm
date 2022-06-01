import sys
input = sys.stdin.readline

def factorial(n):  # n!값을 리턴하는 함수
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

N = int(input())

print(factorial(N))