n = int(input())  # 지도의 크기
plan = input().split()  # 이동 계획서

x, y = 1, 1  # 현재 위치

direction = ['L', 'R', 'U', 'D']  # 이동 방향 종류
dx = [-1, 1, 0, 0]  # x축 이동
dy = [0, 0, -1, 1]  # y축 이동

for move in plan:
    # 이동시 위치
    nx = x + dx[direction.index(move)]
    ny = y + dy[direction.index(move)]

    # 지도 안으로만 이동
    if 1 <= nx <= n and 1 <= ny <= n:
        x = nx
        y = ny
    
print(y, x)  # 결과 출력

''' 입력 예시 1
5
R R R U D D
'''
''' 출력 예시 1
3 4
'''