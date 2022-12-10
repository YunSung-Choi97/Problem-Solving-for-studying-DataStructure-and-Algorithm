n, m = map(int, input().split())  # 세로 길이, 가로 길이
graph = [list(map(int, input())) for _ in range(n)]  # 얼음 틀 상태

def dfs(graph, x, y):
    # 막혀있는 칸, 이미 얼음을 채운 칸인 경우
    if graph[y][x] == 1:
        return
    
    graph[y][x] = 1  # 현재 위치는 채운 칸으로 변경

    dx = [1, 0, -1, 0]  # x축 이동
    dy = [0, 1, 0, -1]  # y축 이동

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            dfs(graph, nx, ny)

count = 0  # 생성되는 총 아이스크림의 개수
# 아이스크림 얼리기
for y in range(n):
    for x in range(m):
        if graph[y][x] == 0:
            dfs(graph, x, y)
            count += 1

print(count)  # 결과 출력

''' 입력 예시 1
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''
''' 출력 예시 1
8
'''