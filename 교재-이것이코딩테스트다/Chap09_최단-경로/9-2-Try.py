import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
X, K = map(int, input().split())

INF = M+1

def path_toK(start):
    distance = [INF] * (N+1)
    distance[start] = 0
    min_heap = []
    heapq.heappush(min_heap, (0, start))
    while min_heap:
        dist, now = heapq.heappop(min_heap)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            new = dist + 1
            if new < distance[i]:
                distance[i] = new
                heapq.heappush(min_heap, (distance[i], i))
    return distance[K]

def path_toX(start):
    distance = [INF] * (N+1)
    distance[start] = 0
    min_heap = []
    heapq.heappush(min_heap, (0, start))
    while min_heap:
        dist, now = heapq.heappop(min_heap)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            new = dist + 1
            if new < distance[i]:
                distance[i] = new
                heapq.heappush(min_heap, (distance[i], i))
    return distance[X]

toK = path_toK(1)
if toK == INF:
    print(-1)
else:
    toX = path_toX(K)
    if toX == INF:
        print(-1)
    else:
        print(toK + toX)