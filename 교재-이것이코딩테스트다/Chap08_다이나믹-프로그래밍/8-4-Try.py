N = int(input())

if N == 1:
    print(1)
else:
    dp = [0] * (N+1)
    dp[1] = 1
    for i in range(2, N+1):
        if i % 2 == 0:
            dp[i] = dp[i-2] + 3
        else:
            dp[i] = dp[i-1] + 2
    print(dp[N] % 796796)