# 피보나치 수열 함수
def fibonacci(n):
    f = [0] * (n + 1)
    f[1], f[2] = 1, 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

n = int(input())  # n 입력받기
print(fibonacci(n), n - 2)  # 결과 출력 (재귀호출 시 계산 수, 동적 프로그래밍 시 계산 수)