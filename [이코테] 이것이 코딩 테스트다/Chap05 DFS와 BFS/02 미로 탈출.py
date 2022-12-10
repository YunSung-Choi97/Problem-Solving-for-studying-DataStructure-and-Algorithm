from collections import deque

n, m = map(int, input().split())  # 세로 길이, 가로 길이
graph = [list(map(int, input())) for _ in range(n)]  # 괴물 위치 정보

visited = [[False] * m for _ in range(n)]  # 방문 확인 및 거리 기록

def bfs(graph, visited):
    # bfs를 위한 큐 생성
    queue = deque()

    dx = [1, 0, -1, 0]  # x축 이동
    dy = [0, 1, 0, -1]  # y축 이동

    # 시작 위치 추가와 방문 처리
    queue.append((0, 0))
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 미로 바깥 영역인 경우
            if nx < 0 or m <= nx or ny < 0 or n <= ny:
                continue
            # 괴물이 있는 구역인 경우
            if graph[ny][nx] == 0:
                continue
            # 이미 방문한 구역인 경우
            if visited[ny][nx]:
                continue
            # 다음 위치 추가와 방문 처리
            queue.append((nx, ny))
            visited[ny][nx] = visited[y][x] + 1

bfs(graph, visited)  # 시작점에서 bfs 시작
print(visited[-1][-1])  # 출구까지의 거리 출력

''' 입력 예시 1
5 6
101010
111111
000001
111111
111111
'''
''' 출력 예시 1
10
'''