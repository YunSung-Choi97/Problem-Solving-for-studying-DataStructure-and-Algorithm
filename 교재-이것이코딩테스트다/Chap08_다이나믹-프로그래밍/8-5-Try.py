N, M = map(int, input().split())
money = [int(input()) for _ in range(N)]
money.sort(reverse=True)

dp = [-1] * (M+1)
dp[0] = 0
for cost in range(1, M+1):
    for i in range(N):
        if cost - money[i] < 0:
            continue
        if dp[cost] == -1 and dp[cost - money[i]] != -1:
            dp[cost] = dp[cost - money[i]] + 1
        elif dp[cost - money[i]] != -1:
            dp[cost] = min(dp[cost], dp[cost - money[i]] + 1)

print(dp[-1])