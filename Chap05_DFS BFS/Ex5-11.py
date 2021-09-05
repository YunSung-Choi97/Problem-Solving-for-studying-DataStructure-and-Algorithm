import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

visited = [[False for j in range(M)] for i in range(N)]


def bfs(x, y, count):
    if x <= -1 or x >= M or y <= -1 or y >= N:
        return
    
    if graph[y][x] == 1 and visited[y][x] == False:
        queue.append((x, y, count))
        visited[y][x] = True

result = 0
queue = deque()
bfs(0, 0, 0)
while queue:
    new_x, new_y, new_count = queue.popleft()
    if new_x == M-1 and new_y == N-1:
        result = new_count
        break
    bfs(new_x+1, new_y, new_count+1)
    bfs(new_x-1, new_y, new_count+1)
    bfs(new_x, new_y+1, new_count+1)
    bfs(new_x, new_y-1, new_count+1)

print(result+1)