'''미리 생각하기
1. 입력받기
2. 오른쪽으로 진행하는 함수 제작
 2-1. (i, j)에서 어디로 이동할 것인지 정함
 2-2. 도착한 곳 True
 2-3. 가다가 길이 막히면 돌아옴 (BackTracking)
'''

import sys

R, C = map(int, input().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

# 파이프가 연결된 상태 확인. 첫 열은 파이프가 모두 연결될 수 있으므로 True로 초기화
arrived = [[True] + [False for i in range(1, C)] for j in range(R)]
dy = [-1, 0, 1]
def route(r, c):
    # 다음 열이 마지막 열인 경우
    if c + 1 == C - 1:
        global count, flag
        count += 1
        flag = True
        return

    # 오른쪽 위 대각선, 오른쪽, 오른쪽 아래 대각선 순서로 확인
    for i in range(3):
        # 이동할 좌표
        nr, nc = r + dy[i], c + 1

        # 격자 범위 밖 제외
        if not (0 <= nr < R and 0 <= nc < C):
            continue
        # 못가는 위치 or 이미 방문한 위치 제외
        if graph[nr][nc] == 'x' or arrived[nr][nc] == True:
            continue
        
        arrived[nr][nc] = True  # 방문 처리
        route(nr, nc)
        if flag: return

count = 0  # 연결된 파이프 수
for y in range(R):
    flag = False  # 파이프 연결 상태
    route(y, 0)

# 정답 출력
print(count)