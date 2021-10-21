import sys
input = sys.stdin.readline

# 입력받기
n = int(input())
data_set = [list(map(int, input().split())) for i in range(n)]

# 합이 최대가 되는 경로를 탐색
Sn = [[0 for _ in range(i)] for i in range(1, n + 1)]
Sn[0][0] = data_set[0][0]

for i in range(1, n):
    Sn[i][0] = Sn[i - 1][0] + data_set[i][0]
    Sn[i][i] = Sn[i - 1][i - 1] + data_set[i][i]
    for j in range(1, i):
        Sn[i][j] = max(Sn[i - 1][j - 1] + data_set[i][j], Sn[i - 1][j] + data_set[i][j])

# 정답 출력
print(max(Sn[n - 1]))