import sys
input = sys.stdin.readline

# 입력받기
n = int(input())
data = [0] + [int(input()) for _ in range(n)]

# n이 1 또는 2인 경우는 계산 X
if n == 1:
    print(data[1])
elif n == 2:
    print(data[1] + data[2])
else:
    # dp 초기화
    dp = [0] * (n + 1)
    dp[1] = data[1]
    dp[2] = data[1] + data[2]

    # dp 계산
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 4] + data[i - 2] + data[i - 1], dp[i - 2] + data[i], dp[i - 3] + data[i - 1] + data[i])
    
    # 결과 출력
    print(dp[n])