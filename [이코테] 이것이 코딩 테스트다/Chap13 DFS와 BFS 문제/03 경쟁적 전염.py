from collections import deque

N, K = map(int, input().split())  # 시험관 크기, 바이러스 종류
board = []  # 시험관 정보
for _ in range(N):
    board.append(list(map(int, input().split())))
S, Y, X = map(int, input().split())  # 증식 시간, 위치(X, Y)

virus = []  # 바이러스 정보
for y in range(N):
    for x in range(N):
        if board[y][x] != 0:
            virus.append((board[y][x], (x, y), 0))
virus.sort()  # 종류의 번호가 낮은 바이러스부터 증식하기위해 정렬
virus = deque(virus)  # 정렬 후 큐에 저장

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def increase_virus(x, y, virus_type, time):
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        # 시험관 내부가 아닌 경우 통과
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        # 증식할 위치에 바이러스가 이미 존재하는 경우 통과
        if board[ny][nx] != 0:
            continue
        board[ny][nx] = virus_type  # 바이러스 증식
        virus.append((virus_type, (nx, ny), time + 1))  # 추가된 바이러스 정보 저장

while virus:
    virus_type, location, time = virus.popleft()
    # 확인 지점이 증식된 경우 탐색 종료
    if location[0] == X - 1 and location[1] == Y - 1:
        break
    # 증식 시간이 지난 경우 탐색 종료
    if time >= S:
        break
    increase_virus(location[0], location[1], virus_type, time)

print(board[Y - 1][X - 1])  # 결과 출력

''' 입력 예시 1
3 3
1 0 2
0 0 0
3 0 0
2 3 2
'''
''' 출력 예시 1
3
'''

''' 입력 예시 2
3 3
1 0 2
0 0 0
3 0 0
1 2 2
'''
''' 출력 예시 2
0
'''