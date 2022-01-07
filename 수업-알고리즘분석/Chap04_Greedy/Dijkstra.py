INF = 1000

w = [[0, 7, 4, 6, 1], [INF, 0, INF, INF, INF], [INF, 2, 0, 5, INF], [INF, 3, INF, 0, INF], [INF, INF, INF, 1, 0]]
n = 5

visited = [False] * n
length = [INF] * n

visited[0] = True
for i in range(n):
    length[i] = w[0][i]

for i in range(n - 1):
    now = 3