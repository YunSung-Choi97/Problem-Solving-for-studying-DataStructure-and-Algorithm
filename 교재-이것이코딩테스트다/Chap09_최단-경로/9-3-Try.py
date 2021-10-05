import sys
from queue import PriorityQueue
input = sys.stdin.readline

N, M, C = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))

INF = M * 1000 + 1
distance = [INF] * (N + 1)

def path(start):
    distance[start] = 0
    PQ = PriorityQueue()
    PQ.put((0, start))
    while not PQ.empty():
        dist, now = PQ.get()
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                PQ.put((distance[i[0]], i[0]))

path(C)
count, max_time = 0, 0
for i in range(1, N+1):
    if distance[i] != INF:
        count += 1
    if distance[i] != INF and distance[i] > max_time:
        max_time = distance[i]
print(count - 1, max_time)