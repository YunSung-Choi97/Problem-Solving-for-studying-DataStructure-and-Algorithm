from collections import deque

# 국경선을 열 나라들 확인
def bfs(location):
    queue = deque()  # 탐색할 지역
    queue.append(location)
    visited[location[1]][location[0]] = True  # 방문 처리
    union_country = [location]  # 연합된 지역
    union_population = board[location[1]][location[0]]  # 연합된 지역의 전체 인구
    union_count = 1  # 연합된 국가의 수

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            # 땅을 벗어난 경우 통과
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            # 이미 방문한 나라인 경우 통과
            if visited[ny][nx]:
                continue
            # 인구 차이가 범위 안인 경우
            if L <= abs(board[y][x] - board[ny][nx]) <= R:
                queue.append((nx, ny))  # 탐색할 지역 추가
                visited[ny][nx] = True  # 방문한 지역 처리
                union_country.append((nx, ny))  # 연합된 지역 처리
                union_population += board[ny][nx]  # 연합된 지역의 인구 추가
                union_count += 1  # 연합된 국가 수 추가
    
    return (union_country, union_population, union_count)  # 연합된 지역 반환

N, L, R = map(int, input().split())  # 땅의 크기, 인구수 차이의 최소값과 최대값
board = []  # 나라별 인구 수
for _ in range(N):
    board.append(list(map(int, input().split())))

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
day = 0
while True:
    visited = [[False for x in range(N)] for y in range(N)]  # 방문한 지역인지 저장
    union_result = []
    # 연합할 국가들 확인
    for y in range(N):
        for x in range(N):
            # 이미 방문한 나라인 경우 통과
            if visited[y][x]:
                continue
            union_result.append(bfs((x, y)))

    # 연합된 국가가 없는 경우 인구 이동 종료
    if len(union_result) == N * N:
        break
    # 연합된 국가간에 인구 이동
    for countries in union_result:
        # 독립 국가인 경우 통과
        if countries[2] == 1:
            continue
        for i in range(countries[2]):
            board[countries[0][i][1]][countries[0][i][0]] = countries[1] // countries[2]
    
    day += 1  # 하루 경과

print(day)  # 결과 출력

''' 입력 예시 1
2 20 50
50 30
20 40
'''
''' 출력 예시 1
1
'''

''' 입력 예시 2
2 40 50
50 30
20 40
'''
''' 출력 예시 2
0
'''

''' 입력 예시 3
2 20 50
50 30
30 40
'''
''' 출력 예시 3
1
'''

''' 입력 예시 4
3 5 10
10 15 20
20 30 25
40 22 10
'''
''' 출력 예시 4
2
'''

''' 입력 예시 5
4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10
'''
''' 출력 예시 5
3
'''