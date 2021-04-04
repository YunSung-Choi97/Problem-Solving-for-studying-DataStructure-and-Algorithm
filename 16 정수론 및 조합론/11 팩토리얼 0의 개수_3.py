# 런타임 에러 (RecursionError) 발생
import sys
input = sys.stdin.readline

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

N = int(input())

N_fac = factorial(N)

# 10으로 나눠 나머지가 0인 경우는 끝자리가 0인것을 의미
count = 0
while N_fac % 10 == 0:
    count += 1
    N_fac //= 10
print(count)