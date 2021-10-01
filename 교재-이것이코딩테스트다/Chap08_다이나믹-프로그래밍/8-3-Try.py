N = int(input())
data = list(map(int, input().split()))

dp = [0] * N
dp[0] = data[0]
dp[1] = data[1]
dp[2] = data[0] + data[2]

for i in range(3, N):
    dp[i] = max(dp[i-3] + data[i], dp[i-2] + data[i])

print(max(dp[-1], dp[-2]))