import sys
input = sys.stdin.readline

d = 1000000007

def fibonacci(n):
    (n2, n1) = 0, 1
    for _ in range(n-1):
        (n2, n1) = (n1 % d, (n2 + n1) % d)
    return n1

N = int(input())
if N == 1:
    print(1)
elif N == 2:
    print(1)
else:
    print(fibonacci(N))