import copy

N, K = map(int, input().split())  # 시험관 크기, 바이러스 종류
board = []  # 시험관 정보
for _ in range(N):
    board.append(list(map(int, input().split())))
S, Y, X = map(int, input().split())  # 증식 시간, 위치(X, Y)

virus = [[] for _ in range(K + 1)]  # 현재 증식가능한 바이러스 종류별 위치: 번호가 낮은 바이러스부터 증식시키기 위해 저장
new_virus = [[] for _ in range(K + 1)]  # 다음 증식가능한 바이러스 종류별 위치
for y in range(N):
    for x in range(N):
        if board[y][x] != 0:
            virus[board[y][x]].append((x, y))
            new_virus[board[y][x]].append((x, y))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def increase_virus(x, y, virus_type):
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        # 시험관 내부가 아닌 경우 통과
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        # 증식할 위치에 바이러스가 이미 존재하는 경우 통과
        if board[ny][nx] != 0:
            continue
        board[ny][nx] = virus_type  # 바이러스 증식
        new_virus[virus_type].append((nx, ny))  # 추가된 바이러스 정보 저장
    new_virus[virus_type].remove((x, y))  # 증식했기 때문에 이후에 증식이 불가능하므로 제거

for time in range(S):  # S번 증식
    # time초의 바이러스 증식 시작
    for virus_type in range(1, K + 1):  # 바이러스 번호가 낮은 바이러스부터 차례로 증식
        for x, y in virus[virus_type]:
            increase_virus(x, y, virus_type)
    virus = copy.deepcopy(new_virus)  # 증식된 바이러스 정보 불러오기

print(board[Y - 1][X - 1])  # 결과 출력