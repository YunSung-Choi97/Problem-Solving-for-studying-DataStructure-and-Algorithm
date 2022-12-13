INF = int(1e9)

n, m = map(int, input().split())  # 회사 개수, 경로 개수

graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 회사 간 연결된 경로
for i in range(1, n + 1):
    graph[i][i] = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())  # 목적지 위치, 경유지 위치

# 플로이드 워셜 알고리즘
for start in range(1, n + 1):
    for end in range(1, n + 1):
        for mid in range(1, n + 1):
            graph[start][end] = min(graph[start][end], graph[start][mid] + graph[mid][end])

# 결과 출력
if graph[1][k] == INF or graph[k][x] == INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])

''' 입력 예시 1
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
'''
''' 출력 예시 1
3
'''

''' 입력 예시 2
4 2
1 3
2 4
3 4
'''
''' 출력 예시 2
-1
'''