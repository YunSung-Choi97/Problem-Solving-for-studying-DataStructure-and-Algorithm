import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
time = [0 for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]
for i in range(N):
    data = list(map(int, input().split()))
    data.pop()
    time[i + 1] = data[0]
    for pre in data[1:]:
        graph[pre].append(i + 1)
        indegree[i + 1] += 1

Queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        Queue.append(i)

result = time[:]
while Queue:
    start = Queue.popleft()
    for end in graph[start]:
        result[end] = max(result[end], result[start] + time[end])
        indegree[end] -= 1
        if indegree[end] == 0:
            Queue.append(end)


for i in range(1, N + 1):
    print(result[i])