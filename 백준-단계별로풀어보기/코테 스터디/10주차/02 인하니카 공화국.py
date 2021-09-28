import sys
input = sys.stdin.readline

def dfs(n, cost):
    visited[n] = True
    
    leafs = []
    for i in range(len(graph[n])):
        node = graph[n][i][0]
        if not visited[node]:
            leafs.append(graph[n][i])
    
    if len(leafs) == 0:  # 하위 노드가 없는 경우
        return cost
    
    ncost = 0  # 하위 노드들의 다리 폭파 비용 합
    for leaf in leafs:
        ncost += dfs(leaf[0], leaf[1])
    
    if cost > ncost:  # ( 상위 노드와 연결비용 Vs. 하위 노드 전체 연결비용 ) 더 저렴한 비용을 이용
        return ncost
    else:
        return cost

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        node1, node2, cost = map(int, input().split())
        graph[node1].append((node2, cost))
        graph[node2].append((node1, cost))

    visited = [False] * (N+1)
    start = 0  # 첫번째(1번노드)는 상위노드가 없으므로, 연결된 모든 노드들을 폭파하는 경우를 초기비용으로 고려
    for i in range(len(graph[1])):
        start += graph[1][i][1]

    print(dfs(1, start))