from itertools import combinations
from copy import deepcopy

# 3개의 장애물이 설치된 복도 생성
def make_obstacle(board):
    # 장애물이 설치된 복도 생성
    obstacle_board = deepcopy(board)
    for i in range(3):
        obstacle_board[location[i][0]][location[i][1]] = 'O'
    return obstacle_board

# direction 방향으로 학생이 있는지 확인
def find_student(board, location, direction):
    ny, nx = location[0] + direction[0], location[1] + direction[1]
    # 벽까지 모두 확인한 경우
    if not (0 <= nx < N and 0 <= ny < N):
        return False
    # 장애물까지 모두 확인한 경우
    if board[ny][nx] == 'O':
        return False
    # 학생을 발견한 경우
    if board[ny][nx] == 'S':
        return True
    # direction 방향으로 더 확인
    return find_student(board, (ny, nx), direction)

N = int(input())  # 복도의 크기
board = []  # 복도 정보 (T: 선생님, S: 학생, X: 빈 공간)
for _ in range(N):
    board.append(list(map(str, input().split())))

blank, teacher = [], []  # 빈 공간, 선생님 위치정보 저장
for y in range(N):
    for x in range(N):
        if board[y][x] == 'X':
            blank.append((y, x))
        if board[y][x] == 'T':
            teacher.append((y, x))

for location in combinations(blank, 3):
    result = True  # 모든 학생들이 감시로부터 피할수 있다고 가정
    obstacle_board = make_obstacle(board)  # 장애물이 설치된 복도 생성
    for teacher_location in teacher:
        # 선생님 위치의 위쪽 방향에서 학생을 발견된 경우 탐색 종료
        if find_student(obstacle_board, teacher_location, (-1, 0)):
            result = False
            break
        # 선생님 위치의 아래쪽 방향에서 학생을 발견된 경우 탐색 종료
        if find_student(obstacle_board, teacher_location, (1, 0)):
            result = False
            break
        # 선생님 위치의 오른쪽 방향에서 학생을 발견된 경우 탐색 종료
        if find_student(obstacle_board, teacher_location, (0, 1)):
            result = False
            break
        # 선생님 위치의 왼쪽 방향에서 학생을 발견된 경우 탐색 종료
        if find_student(obstacle_board, teacher_location, (0, -1)):
            result = False
            break
    # 모든 학생들이 감시를 피하는 경우 발견
    if result:
        break

# 결과 출력
if result:
    print('YES')
else:
    print('NO')

''' 입력 예시 1
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X
'''
''' 출력 예시 1
YES
'''

''' 입력 예시 2
4
S S S T
X X X X
X X X X
T T T X
'''
''' 출력 예시 2
NO
'''