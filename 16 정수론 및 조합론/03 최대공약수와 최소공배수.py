import sys
input = sys.stdin.readline

# 최대공약수를 구하는 함수
def gcd(num1, num2):
    if num1 < num2:
        (num1, num2) = (num2, num1)
    while num2 != 0:
        (num1, num2) = (num2, num1 % num2)
    return num1

N, M = map(int, input().split())

GCD = gcd(N, M)  # N과 M의 최대공약수 GCD

# 최대공약수와 최소공배수 출력 (최소공배수 = N x M / GCD)
print(GCD)
print(N * M // GCD)