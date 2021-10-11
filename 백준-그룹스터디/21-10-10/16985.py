import sys
from itertools import permutations
from collections import deque
input = sys.stdin.readline

# board를 rot에 따라 회전시키는 함수
def rotation(board, rot):
    # rot의 값에 따라 회전 => (0 : 0도, 1 : 90도, 2 : 180도, 3 : 270도)
    if rot == 0:
        return board
    result = [[0 for j in range(5)] for i in range(5)]  # 회전된 board 정보를 저장할 2차원 리스트
    for y in range(5):
        for x in range(5):
            if rot == 1:
                nx = y
                ny = 4 - x
            elif rot == 2:
                nx = 4 - x
                ny = 4 - y
            elif rot == 3:
                nx = 4 - y
                ny = x
            result[ny][nx] = board[y][x]
    return result

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
# bfs방식으로 큐브 탐색 (0, 0, 0) -> (4, 4, 4)
def bfs():
    if cube[0][0][0] == 0:  # 진입 불가
        return INF
    queue = deque()
    route = [[[INF for k in range(5)] for j in range(5)] for i in range(5)]  # 현재까지의 최단경로
    queue.append((0, 0, 0))
    route[0][0][0] = 0
    while queue:
        z, y, x = queue.popleft()
        for d in range(6):
            nz = z + dz[d]
            ny = y + dy[d]
            nx = x + dx[d]
            if not (0 <= nx <= 4 and 0 <= ny <= 4 and 0 <= nz <= 4):  # 큐브 밖
                continue
            if cube[nz][ny][nx] == 0:  # 들어갈 수 없는 칸
                continue
            if route[nz][ny][nx] != INF:  # 이미 방문한 칸
                continue

            queue.append((nz, ny, nx))
            route[nz][ny][nx] = route[z][y][x] + 1
            if nz == 4 and ny == 4 and nx == 4:  # 목적지 도착
                return route[nz][ny][nx]
            if route[nz][ny][nx] > result:  # 더 짧은 경로 존재
                return INF
    return INF  # 경로탐색 실패

boards = [[list(map(int, (input().split()))) for line in range(5)] for board in range(5)]
case = permutations(range(5), 5)
cube = [0] * 5
INF = 5 * 5 * 5
result = INF
for floor in case:  # 각 층에 들어갈 보드 정하기
    for fir in range(4):  # 1층 회전
        cube[0] = rotation(boards[floor[0]], fir)
        for sec in range(4):  # 2층 회전
            cube[1] = rotation(boards[floor[1]], sec)
            for thi in range(4):  # 3층 회전
                cube[2] = rotation(boards[floor[2]], thi)
                for fou in range(4):  # 4층 회전
                    cube[3] = rotation(boards[floor[3]], fou)
                    for fif in range(4):  # 5층 회전
                        cube[4] = rotation(boards[floor[4]], fif)
                        
                        temp = bfs()  # 현재 큐브에서의 최단경로
                        if result > temp:
                            result = temp
                        if result == 12:  # 최단경로 중 12가 최소이므로 탐색종료
                            print(12)
                            sys.exit()

if result == INF:  # 경로탐색 실패
    print(-1)
else:  # 최단경로 출력
    print(result)