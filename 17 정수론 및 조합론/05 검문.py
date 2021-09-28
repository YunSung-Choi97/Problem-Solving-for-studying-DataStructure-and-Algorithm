import sys
input = sys.stdin.readline

# 최대공약수를 구하는 함수
def gcd(num1, num2):
    if num1 < num2:
        (num1, num2) = (num2, num1)
    while num2 != 0:
        (num1, num2) = (num2, num1 % num2)
    return num1

# 약수를 구하는 함수
def factor(num):
    factor_list = []

    # 반복문을 num의 제곱근까지만 해줌.
    for Q in range(1, int(num**0.5) + 1):
        if num % Q == 0:
            factor_list.append(Q)
            if Q * Q != num:  # 제곱수인 경우에 같은 수가 두번 입력되는 것을 막기 위함.
                factor_list.append(num//Q)
    factor_list.sort()
    return factor_list

N = int(input())  # 입력받을 수의 개수

num_list = []  # 입력받은 수를 저장하는 리스트
for _ in range(N):
    num_list.append(int(input()))
num_list.sort()

num_dif = []  # 입력받은 수들 사이의 차를 저장하는 리스트 (이웃한 인덱스사이의 차만 저장)
for i in range(N-1):
    num_dif.append(num_list[i+1] - num_list[i])

# "이웃한 수의 차"들의 최대공약수를 구해준 후 약수를 결과에 저장
if N == 2:
    result = factor(num_dif[0])
else:
    GCD = num_dif[0]
    for i in range(1, N-1):
        GCD = gcd(GCD, num_dif[i])
    result = factor(GCD)

# 결과 중 1을 제외한 값을 출력
for M in result[1:]:
    print(M, end=' ')