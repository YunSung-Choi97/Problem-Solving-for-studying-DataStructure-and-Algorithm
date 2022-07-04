import sys
input = sys.stdin.readline

# 문제정보 입력받기
N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

# 2차원 배열의 누적 합 계산
prefix_sum = [[0 for i in range(N + 1)] for j in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + table[i - 1][j - 1]

# 결과 출력
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(prefix_sum[x2][y2] - prefix_sum[x2][y1 - 1] -prefix_sum[x1 - 1][y2] + prefix_sum[x1 - 1][y1 - 1])