from collections import deque

# 로봇이 이동가능한 위치인지 확인
def can_move(board, visited, location1, location2, size):
    # 이동 위치가 지도 밖인 경우 통과
    if not (0 <= location1[1] < size and 0 <= location1[0] < size and 0 <= location2[1] < size and 0 <= location2[0] < size):
        return False
    # 이동 위치에 벽이 존재하는 경우 통과
    if board[location1[0]][location1[1]] == 1 or board[location2[0]][location2[1]] == 1:
        return False
    # 이동 위치가 이미 방문한 위치인 경우 통과
    if ((location1[0], location1[1]), (location2[0], location2[1])) in visited or ((location2[0], location2[1]), (location1[0], location1[1])) in visited:
        return False
    return True

# 방문할 위치에 추가
def push_queue(queue, visited, next_location1, next_location2, next_time):
    queue.append((next_location1, next_location2, next_time))  # 방문할 위치에 추가
    visited.append((next_location1, next_location2))  # 방문 처리

# 로봇 한 칸 이동
def move_robot(board, visited, queue, location1, location2, time, size):
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    # 상, 하, 좌, 우로 이동
    for d in range(4):
        nx1, ny1 = location1[1] + dx[d], location1[0] + dy[d]
        nx2, ny2 = location2[1] + dx[d], location2[0] + dy[d]
        # 이동할 위치가 맞는지 확인 후 맞다면 이동할 위치 추가
        if can_move(board, visited, (ny1, nx1), (ny2, nx2), size):
            push_queue(queue, visited, (ny1, nx1), (ny2, nx2), time + 1)

# 로봇 회전
def rotate_robot(board, visited, queue, location1, location2, time, size):
    # 로봇이 가로로 배치된 경우
    if location1[0] == location2[0]:
        # location1을 축으로 시계방향으로 회전이 가능한 경우 회전
        if can_move(board, visited, (location1[0], location1[1]), (location1[0] + 1, location1[1]), size) and board[location2[0] + 1][location2[1]] == 0:
            push_queue(queue, visited, (location1[0], location1[1]), (location1[0] + 1, location1[1]), time + 1)
        # location1을 축으로 반시계방향으로 회전이 가능한 경우 회전
        if can_move(board, visited, (location1[0], location1[1]), (location1[0] - 1, location1[1]), size) and board[location2[0] - 1][location2[1]] == 0:
            push_queue(queue, visited, (location1[0], location1[1]), (location1[0] - 1, location1[1]), time + 1)
        # location2을 축으로 시계방향으로 회전이 가능한 경우 회전
        if can_move(board, visited, (location2[0] - 1, location2[1]), (location2[0], location2[1]), size) and board[location1[0] - 1][location1[1]] == 0:
            push_queue(queue, visited, (location2[0] - 1, location2[1]), (location2[0], location2[1]), time + 1)
        # location2을 축으로 반시계방향으로 회전이 가능한 경우 회전
        if can_move(board, visited, (location2[0] + 1, location2[1]), (location2[0], location2[1]), size) and board[location1[0] + 1][location1[1]] == 0:
            push_queue(queue, visited, (location2[0] + 1, location2[1]), (location2[0], location2[1]), time + 1)
    # 로봇이 세로로 배치된 경우
    else:
        # location1을 축으로 시계방향으로 회전이 가능한 경우 회전
        if can_move(board, visited, (location1[0], location1[1]), (location1[0], location1[1] - 1), size) and board[location2[0]][location2[1] - 1] == 0:
            push_queue(queue, visited, (location1[0], location1[1]), (location1[0], location1[1] - 1), time + 1)
        # location1을 축으로 반시계방향으로 회전이 가능한 경우 회전
        if can_move(board, visited, (location1[0], location1[1]), (location1[0], location1[1] + 1), size) and board[location2[0]][location2[1] + 1] == 0:
            push_queue(queue, visited, (location1[0], location1[1]), (location1[0], location1[1] + 1), time + 1)
        # location2을 축으로 시계방향으로 회전이 가능한 경우 회전
        if can_move(board, visited, (location2[0], location2[1] + 1), (location2[0], location2[1]), size) and board[location1[0]][location1[1] + 1] == 0:
            push_queue(queue, visited, (location2[0], location2[1] + 1), (location2[0], location2[1]), time + 1)
        # location2을 축으로 반시계방향으로 회전이 가능한 경우 회전
        if can_move(board, visited, (location2[0], location2[1] - 1), (location2[0], location2[1]), size) and board[location1[0]][location1[1] - 1] == 0:
            push_queue(queue, visited, (location2[0], location2[1] - 1), (location2[0], location2[1]), time + 1)

def solution(board):
    size = len(board)
    visited = []  # 방문한 위치인지 확인
    queue = deque()  # 이동 가능한 위치/시간 정보 저장: ((y1, x1), (y2, x2), time)
    queue.append(((0, 0), (0, 1), 0))  # 출발 위치와 시간 저장: (0, 0), (0, 1), 0
    
    while queue:
        location1, location2, time = queue.popleft()
        # (N, N) 위치에 로봇이 도착한 경우 최소 시간 반환
        if location1 == (size - 1, size - 1) or location2 == (size - 1, size - 1):
            return time
        move_robot(board, visited, queue, location1, location2, time, size)
        rotate_robot(board, visited, queue, location1, location2, time, size)

# print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
''' 입력 예시 1
[[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
'''
''' 출력 예시 1
7
'''