'''미리 생각하기
1. 입력받기
2. 오른쪽으로 진행하는 함수 제작
 2-1. (i, j)에서 어디로 이동할 것인지 정함
 2-2. 도착한 곳 True
'''

# Greedy ?? 느낌으로 모든 파이프를 갈 수 있는 곳으로 계속해서 연결해서 진행한 결과 Test case가 모두 동작.
# 그러나, 아래와 같은 상황처럼 위쪽 길이 막히고 아래쪽 길은 안막힌 상황에서 아래쪽 길로 가는 다른 파이프가 없다면 틀린 결과가 나타남.
# 그리디 정당성에 대한 고려가 부족.
# .x.x.
# ..xx.
# .x...

import sys

R, C = map(int, input().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

# 파이프가 연결된 상태 확인. 첫 열은 파이프가 모두 연결될 수 있으므로 True로 초기화
arrived = [[True] + [False for i in range(1, C)] for j in range(R)]
dy = [-1, 0, 1]
def route(r, c):
    # 오른쪽 위 대각선, 오른쪽, 오른쪽 아래 대각선 순서로 확인
    for i in range(3):
        # 이동할 좌표
        nr, nc = r + dy[i], c + 1
        if not (0 <= nr < R and 0 <= nc < C):  # 격자 범위 밖 제외
            continue

        # 연결이 가능하고, 아직 연결되지 않은 지점인 경우
        if graph[nr][nc] == '.' and arrived[nr][nc] == False:
            arrived[nr][nc] = True
            return None

# 마지막 열 전까지 수행
for x in range(C-1):
    # 한 칸씩 아래로 이동
    for y in range(R):
        # 현재 위치까지 파이프 연결이 안된 경우 제외
        if not arrived[y][x]:
            continue
        route(y, x)

# 마지막 열까지 연결된 파이프 수 확인
count = 0
for i in range(R):
    if arrived[i][C-1]:
        count += 1

# 정답 출력
print(count)