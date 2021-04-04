import sys
input = sys.stdin.readline

# 최대공약수를 구하는 함수
def gcd(num1, num2):
    if num1 < num2:
        (num1, num2) = (num2, num1)
    while num2 != 0:
        (num1, num2) = (num2, num1 % num2)
    return num1

T = int(input())  # T : 테스트 케이스의 개수

# 테스트 케이스에 대하여, A와 B의 최대공약수 GCD를 구한 후 LCM (A x B / GCD) 출력
for _ in range(T):
    A, B = map(int, input().split())
    GCD = gcd(A, B)
    print(A * B // GCD)