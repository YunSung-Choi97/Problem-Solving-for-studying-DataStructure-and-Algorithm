N = int(input())

dp = [0, 1, 2]  # N이 1일때는 1가지, 2일때는 2가지
for i in range(3, N + 1):
    result = dp[i - 2] + dp[i - 1]
    dp.append(result % 15746)  # 수열의 개수를 15746으로 나눈 나머지 저장

print(dp[N])