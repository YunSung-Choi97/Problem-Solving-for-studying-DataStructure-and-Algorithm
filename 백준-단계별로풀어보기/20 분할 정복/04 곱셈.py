import sys
input = sys.stdin.readline

# A^N 계산할 때
# N이 짝수라면 (A^(N//2))^2을 이용해 계산을 하고
# N이 홀수라면 (A^(N//2))^2*A를 이용해 계산을 해주었다.
def multiplication_R_by_power(a, b, c):
    if b == 1:
        return a % c
    else:
        root = power(a, b // 2, c)
        if b % 2 == 0:
            return root * root % c
        else:
            return root * root * a % c

A, B, C = map(int, input().split())

print(multiplication_R_by_power(A, B, C))