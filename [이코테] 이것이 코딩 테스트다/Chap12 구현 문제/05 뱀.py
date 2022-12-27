from collections import deque

def move(x, y, d):
    global N, location
    # 방향에 따른 이동량 (E, S, W, N)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    nx, ny = x + dx[d], y + dy[d]  # 이동 후 뱀 머리 위치
    # 벽에 부딪힌 경우
    if not (0 < nx <= N and 0 < ny <= N):
        return False
    # 자기 자신의 몸과 부딪힌 경우
    if (nx, ny) in location:
        return False
    
    # 이동하기
    location.append((nx, ny))  # 머리 이동
    if borad[ny][nx]:
        borad[ny][nx] = 0  # 사과 먹기
    else:
        location.popleft()  # 꼬리 이동
    return True

N = int(input())  # 보드의 크기

K = int(input())  # 사과의 개수
apples = []
for _ in range(K):
    apples.append(tuple(map(int, input().split())))  # 사과의 위치 저장 (행, 열)

L = int(input())  # 뱀의 방향 변환 횟수
rotations = deque()  # 뱀의 방향 전환 정보
for _ in range(L):
    time, direction = input().split()
    rotations.append((int(time), direction))  # 뱀의 방향 전환 정보 저장 (시간, 방향)

# 사과 정보를 보드에 나타내기
borad = [[False] * (N + 1) for _ in range(N + 1)]
for apple in apples:
    borad[apple[0]][apple[1]] = True
# 뱀의 위치정보 나타내기
location = deque()
location.append((1, 1))

time = 0  # 게임 진행 시간
d = 0  # 방향 (E, S, W, N)
while True:
    time += 1
    head_x, head_y = location[-1]  # 뱀 머리 위치
    if not move(head_x, head_y, d):
        break
    if rotations and time == rotations[0][0]:  # 방향 전환 시간인 경우
        # 왼쪽 회전
        if rotations[0][1] == 'L':
            d = (d - 1) % 4
        # 오른쪽 회전
        else:
            d = (d + 1) % 4
        rotations.popleft()

# 게임 종료 시각 출력
print(time)

''' 입력 예시 1
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
'''
''' 출력 예시 1
9
'''

''' 입력 예시 2
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
'''
''' 출력 예시 2
21
'''

''' 입력 예시 3
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
'''
''' 출력 예시 3
13
'''