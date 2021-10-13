'''미리 생각하기
1. 입력받기
 1-1. N, M
 1-2. N x N 크기의 2차원 리스트
2. 블록 그룹 생성 함수
 2-1. 좌표따라 이동
 2-2. 좌표마다 그룹 확인
 2-3. visited 그룹 방문 기록
 2-4. groups에 그룹 크기 기록
3. 중력 함수
4. 반시계 회전 함수
'''
import sys
from collections import deque

# 입력받기
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 블록 그룹 생성 함수
def grouping(r, c):
    # 무지개색, 검은색, 빈칸은 그룹화 하지 않는다.
    if board[r][c] in [0, -1, None]:
        return
    # 이미 그룹으로 묶인 칸은 그룹화 하지 않는다.
    if visited[r][c]:
        return

    # 그룹 생성, 무지개색 블록들 구분, 출발 색상, 탐색 큐, 방문기록
    group, rainbow = [], []  # 그룹들의 좌표, 무지개의 좌표
    color = board[r][c]  # 시작점의 색
    group.append((r, c))
    queue = deque()  # 탐색할 좌표들 저장
    queue.append((r, c))
    visited[r][c] = True  # 시작점은 방문처리
    # BFS
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx and nx < N and 0 <= ny and ny < N):  # 보드 범위내에서만 이동
                continue
            if board[ny][nx] in [color, 0] and not visited[ny][nx]:
                group.append((ny, nx))
                visited[ny][nx] = True
                queue.append((ny, nx))
                if board[ny][nx] == 0:
                    rainbow.append((ny, nx))
    
    score = len(group)
    second_score = len(rainbow)
    if score > 1:
        for i, j in group:
            if board[i][j] == 0 and groups[i][j][0] > score:
                continue
            groups[i][j] = score**2, second_score, (r, c)
    for i, j in rainbow:
        visited[i][j] = False

# 중력 함수
def gravity():
    for x in range(N):
        for y in range(N-1, 0, -1):  # 열 확인 시 아래에서 위로 확인
            if board[y][x] == None:  # 빈칸일 경우
                for ny in range(y-1, -1, -1):
                    if board[ny][x] == -1:
                        break
                    elif board[ny][x] == None:
                        continue
                    else:
                        board[y][x] = board[ny][x]
                        board[ny][x] = None
                        break

# 반시계방향 회전함수
def rotation():
    temp = [[board[i][j] for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            board[i][j] = temp[j][N-1-i]

answer = 0
while True:
    visited = [[False for j in range(N)] for i in range(N)]
    groups = [[(0, 0, (0, 0)) for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            grouping(i, j)

    min_score, min_rainbow, min_location = 1, 0, None
    for i in range(N):
        for j in range(N):
            # 우선순위 비교
            if min_score > groups[i][j][0]:  # 그룹 크기 비교
                continue
            elif min_score == groups[i][j][0]:
                if min_rainbow > groups[i][j][1]:  # 무지개블록 수 비교
                    continue
                elif min_rainbow == groups[i][j][1]:
                    if min_location[0] > groups[i][j][2][0]:  # 행 크기 비교
                        continue
                    elif min_location[0] == groups[i][j][2][0]:
                        if min_location[1] >= groups[i][j][2][1]:  # 열 크기 비교
                            continue
            min_score, min_rainbow, min_location = groups[i][j][0], groups[i][j][1], (i, j)

    # 종료 조건 : 그룹 생성이 안된 경우
    if min_score == 1:
        break
    answer += min_score

    # 블록 그룹 제거
    for i in range(N):
        for j in range(N):
            if min_location == groups[i][j][2]:
                board[i][j] = None
    
    # 중력 작용 >> 반시계방향 회전 >> 중력 작용
    gravity()
    rotation()
    gravity()

print(answer)