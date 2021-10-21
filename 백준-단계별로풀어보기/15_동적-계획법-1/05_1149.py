import sys
input = sys.stdin.readline

N = int(input())  # 집의 수

# costs, color 입력받기
costs = [[0, 0, 0]]  # 색에 따른 집 색칠 비용
for idx in range(1, N + 1):
    RGB = list(map(int, input().split()))
    costs.append(RGB)

INF = 1000 * 1000  # 최대 비용
dp = [[INF, INF, INF] for _ in range(N + 1)]

# 첫번째 집
for i in range(3):
    dp[1][i] = costs[1][i]

# 두번째 ~ N번째 집
for idx in range(2, N + 1):
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            if dp[idx][j] > dp[idx - 1][i] + costs[idx][j]:
                dp[idx][j] = dp[idx - 1][i] + costs[idx][j]

# 정답 출력
print(min(dp[N]))