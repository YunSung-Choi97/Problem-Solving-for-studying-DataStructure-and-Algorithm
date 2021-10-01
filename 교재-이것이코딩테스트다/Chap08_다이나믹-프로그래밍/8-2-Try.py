X = int(input())

dp = [0] * (X+1)

for n in range(2, X+1):
    dp[n] = dp[n-1] + 1
    if n % 5 == 0:
        dp[n] = min(dp[n], dp[n//5] + 1)
    if n % 3 == 0:
        dp[n] = min(dp[n], dp[n//3] + 1)
    if n % 2 == 0:
        dp[n] = min(dp[n], dp[n//2] + 1)

print(dp[X])