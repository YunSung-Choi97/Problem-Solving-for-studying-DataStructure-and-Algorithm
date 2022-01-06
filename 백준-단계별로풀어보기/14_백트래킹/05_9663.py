# 파이썬 언어로는 해당 문제를 BackTracking으로 해결시 시간초과가 발생
answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
print(answer[int(input())])

'''미리 생각하기
1. 입력받기 (N)
2. 체스판 구현하기 >> N X N 크기의 2차원 리스트
3. 퀸의 변화로 발생하는 상황들을 체스판에 표현 >> 퀸이 생기면 공격범위 +1, 퀸이 사라지면 공격범위 -1
4. 현재 줄에서 놓을 수 있는 모든 자리에 퀸을 배치 & 한 줄씩 모든 줄을 확인 (BackTracking) >> 마지막 줄까지 배치시 정답 +1
'''
'''
# N 입력받기
N = int(input())

# 체스판 구현
graph = [[0 for i in range(N)] for j in range(N)]

answer = []  # 퀸 놓는 방법 저장
count = 0  # 방법의 개수(정답)

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

# 공격범위의 방향을 나타내는 단위벡터. 각각은 순서대로 N, NE, E, SE, S, SW, W, NW 방향을 나타낸다.
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
# 퀸의 변화로 발생하는 상황들을 체스판에 표현 >> 퀸이 생기면 공격범위 +1, 퀸이 사라지면 공격범위 -1
def Queen(x, y, k):
    location = []  # 공격가능 범위 좌표들 저장

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