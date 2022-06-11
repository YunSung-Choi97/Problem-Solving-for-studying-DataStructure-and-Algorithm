X = int(input())

# X가 1, 2, 3 중 하나라면 계산 X
if X == 1:
    print(0)
elif X == 2 or X == 3:
    print(1)
else:
    # 연산 횟수 초기화
    INF = int(1e6)
    dp = [INF] * (X + 1)
    dp[1], dp[2], dp[3] = 0, 1, 1

    # 연산 횟수 계산
    for i in range(4, X + 1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1
        if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1
    
    # 결과 출력
    print(dp[X])