import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
data = [input().rstrip() for _ in range(N)]
visited = [[False for x in range(M)] for y in range(N)]
result = 0

def bfs(x0, y0):
    queue = deque()
    queue.append((x0, y0))
    global N, M

    while queue:
        x, y = queue.popleft()
        if visited[y][x]:
            continue
        visited[y][x] = True

        if x == 0 and M == 1:
            pass
        elif x == 0:
            if data[y][x+1] == '0':
                queue.append((x+1, y))
        elif x == M-1:
            if data[y][x-1] == '0':
                queue.append((x-1, y))
        else:
            if data[y][x+1] == '0':
                queue.append((x+1, y))
            if data[y][x-1] == '0':
                queue.append((x-1, y))
        
        if y == 0 and N == 1:
            pass
        elif y == 0:
            if data[y+1][x] == '0':
                queue.append((x, y+1))
        elif y == N-1:
            if data[y-1][x] == '0':
                queue.append((x, y-1))
        else:
            if data[y+1][x] == '0':
                queue.append((x, y+1))
            if data[y-1][x] == '0':
                queue.append((x, y-1))
    
for i in range(N):
    for j in range(M):
        if data[i][j] == '0' and not visited[i][j]:
            result += 1
            bfs(j, i)

print(result)