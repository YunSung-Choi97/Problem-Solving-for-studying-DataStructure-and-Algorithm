import sys
input = sys.stdin.readline

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