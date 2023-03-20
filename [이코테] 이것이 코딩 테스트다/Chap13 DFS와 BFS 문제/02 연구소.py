from itertools import combinations
import copy

# dfs에서 사용할 방향벡터
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# dfs로 바이러스 감염시키기
def dfs(x, y, graph):
    if graph[y][x] == 1:  # 못 가는 구역 통과
        return
    if graph[y][x] == 3:  # 이미 감염된 구역 통과
        return
    graph[y][x] = 3
    for i in range(4):
        if 0 <= x + dx[i] < M and 0 <= y + dy[i] < N:
            dfs(x + dx[i], y + dy[i], graph)

N, M = map(int, input().split())  # 세로 크기, 가로 크기

borad = []  # 연구소 지도 저장 (0: 빈칸, 1: 벽, 2: 바이러스)
blank = []  # 빈칸 위치 저장
for y in range(N):
    row = list(map(int, input().split()))
    borad.append(row)
    for x in range(M):
        if row[x] == 0:
            blank.append((y, x))

result = 0  # 안전 영역의 최대 크기
for a, b, c in combinations(blank, 3):  # 빈칸 중 벽으로 막을 3칸 선택
    duplicated_board = copy.deepcopy(borad)  # 탐색을 위한 복제된 지도
    # 선택된 빈칸 3곳을 벽으로 변경
    duplicated_board[a[0]][a[1]] = 1
    duplicated_board[b[0]][b[1]] = 1
    duplicated_board[c[0]][c[1]] = 1

    for y in range(N):
        for x in range(M):
            if duplicated_board[y][x] == 2:
                dfs(x, y, duplicated_board)

    count = 0  # 3곳을 벽으로 변경했을 때 안전 영역의 크기
    for row in duplicated_board:
        count += row.count(0)
    
    result = max(result, count)

print(result)  # 결과 출력

''' 입력 예시 1
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
'''
''' 출력 예시 1
27
'''

''' 입력 예시 2
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
'''
''' 출력 예시 2
9
'''

''' 입력 예시 3
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
'''
''' 출력 예시 3
3
'''