'''미리 생각하기
1. 입력받기
2. Queue 4개 생성
 2-1. F1 : 방금 생성된 불 위치
 2-2. F2 : 1초뒤 생성될 불 위치
 2-3. H1 : 방금 이동한 위치(들)
 2-4. H2 : 1초뒤 이동할 위치(들)
'''

import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def move(y, x, who):
    global flag
    for i in range(4):
        # 이동할 위치 정하기
        nx, ny = x + dx[i], y + dy[i]
        
        # 이동할 위치가 지도 밖인 경우
        if not (0 <= nx <= w - 1 and 0 <= ny <= h - 1):
            continue
        # 이동할 위치가 벽인 경우
        if graph[ny][nx] == '#':
            continue
        # 불 또는 사람이 방문한 경우
        if Fvisit[ny][nx] or Hvisit[ny][nx]:
            continue
        
        # 이동확인할 대상 확인
        if who == 'fire':
            F2.append((ny, nx))
            Fvisit[ny][nx] = True
        elif who == 'human':
            # 탈출 가능한 위치로 이동하는 경우
            if nx == 0 or nx == w-1 or ny == 0 or ny == h-1:
                flag = True
                return None
            H2.append((ny, nx))
            Hvisit[ny][nx] = True

T = int(input())
for test_case in range(T):
    # 입력받기
    w, h = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(h)]
    
    flag = False  # 탈출 여부
    time = 0  # 이동 횟수
    F1, F2, H1, H2 = deque(), deque(), deque(), deque()
    Fvisit = [[False for j in range(w)] for i in range(h)]
    Hvisit = [[False for j in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '*':
                F1.append((i, j))
                Fvisit[i][j] = True
            elif graph[i][j] == '@':
                H1.append((i, j))
                Hvisit[i][j] = True
                # 시작위치가 탈출구인 경우
                if i == 0 or i == h - 1 or j == 0 or j == w - 1:
                    flag = True
                    time = -1  # 출력 방식때문에 -1로 설정
    
    while H1:
        # 현재 불 >> 생성될 불 위치
        while F1:
            y, x = F1.popleft()
            move(y, x, 'fire')
        # 현재 사람 >> 이동할 사람 위치
        while H1:
            y, x = H1.popleft()
            move(y, x, 'human')
            if flag: break
        
        if flag: break

        # 생성될 불 >> 현재 불
        while H2:
            y, x = H2.popleft()
            H1.append((y, x))
        # 이동할 사람 >> 현재 사람
        while F2:
            y, x = F2.popleft()
            F1.append((y, x))
        
        time += 1

    if flag:
        print(time + 2)  # 탈출구 발견 후 이동 전에 반복문을 탈출하여 + 1, 탈출구에서 탈출까지 + 1
    else:
        print('IMPOSSIBLE')