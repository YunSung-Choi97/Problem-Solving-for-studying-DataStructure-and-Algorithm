n, m = map(int, input().split())  # 맵의 세로 크기, 가로 크기
y, x, direction = map(int, input().split())  # 현재 y 위치, x 위치, 보는 방향

# 맵 정보 입력받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향에 대한
dx = [0, -1, 0, 1]  # x축 이동
dy = [-1, 0, 1, 0]  # y축 이동

visited = [[False] * m for _ in range(n)]  # 방문한 지역 확인

count = 0  # 방문한 칸의 수
while True:
    # 처음온 곳인 경우 방문 처리
    if visited[y][x] == False:
        visited[y][x] = True
        count += 1

    move = False  # 이동 가능한 곳이 있는지 확인
    # 이동 가능한 곳인지 확인 (4가지 방향)
    for d in range(4):
        nd = (direction + d) % 4  # 바라보는 방향
        nx, ny = x + dx[nd], y + dy[nd]  # 이동 위치
        # 이동 위치가 맵 밖인 경우
        if nx < 0 or m <= nx or ny < 0 or n <= ny:
            continue
        # 이동 위치가 바다이거나 방문한 지역인 경우
        if graph[ny][nx] == 1 or visited[ny][nx]:
            continue
        # 이동 가능한 위치 발견한 경우
        move = True
        break

    if move:
        x, y, direction = nx, ny, nd
    else:
        x, y = x + dx[(direction + 2) % 4], y + dy[(direction + 2) % 4]
        if graph[y][x] == 1:
            break

print(count)  # 결과 출력

''' 입력 예시 1
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''
''' 출력 예시 1
3
'''