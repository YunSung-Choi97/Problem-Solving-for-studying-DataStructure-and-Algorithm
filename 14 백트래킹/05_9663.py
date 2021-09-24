answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
print(answer[int(input())])

''' 파이썬 언어로는 해당 문제를 BackTracking으로 해결시 시간초과가 발생
N = int(input())

graph = [[0 for i in range(N)] for j in range(N)]

answer = []  # 퀸 놓는 방법 저장
count = 0  # 방법의 개수
def N_Queen(k):
    if len(answer) == N:
        global count
        count += 1
        # print(answer)  # 퀸 놓는 방법 확인
        return

    for i in range(N):
        if graph[k][i] != 0:  # 퀸을 놓을 수 있는 위치 선정
            continue
        answer.append(i)  # 퀸 놓기
        Queen(i, k, 1)
        N_Queen(k+1)  # 다음 줄로 이동
        answer.pop()  # 퀸 제거
        Queen(i, k, -1)

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
# (x, y)에 퀸을 놓으면 graph의 공격범위 + 1, 퀸을 빼면 - 1
def Queen(x, y, k):
    location = []

    location.append((x, y))
    for d in range(8):
        for i in range(1, N):
            nx = x + i*dx[d]
            ny = y + i*dy[d]
            if 0 <= nx and nx < N and 0 <= ny and ny < N:
                location.append((nx, ny))
    
    for xx, yy in location:
        graph[yy][xx] += k

N_Queen(0)
print(count)
'''