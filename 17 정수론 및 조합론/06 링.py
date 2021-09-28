import sys
input = sys.stdin.readline

# 최대공약수를 구하는 함수
def gcd(num1, num2):
    if num1 < num2:
        (num1, num2) = (num2, num1)
    while num2 != 0:
        (num1, num2) = (num2, num1 % num2)
    return num1

N = int(input())

num_list = list(map(int, input().split()))

for i in range(1, N):
    GCD = gcd(num_list[0], num_list[i])
    print('{}/{}'.format(num_list[0] // GCD, num_list[i] // GCD))  # "(num_list[0] // GCD) / (num_list[i] // GCD)" 출력