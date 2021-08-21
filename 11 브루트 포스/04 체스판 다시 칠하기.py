import sys
input = sys.stdin.readline

def paint_count(data, x0, y0):
    case1 = 0  # 흰색으로 시작
    case2 = 0  # 검은색으로 시작
    for y in range(8):
        for x in range(8):
            if data[y0+y][x0+x] == chess_board[y][x]:
                case1 += 1
            else:
                case2 += 1
    
    return max(case1, case2)

N, M = map(int, input().split())
board_data = []  # 입력받은 보드 정보 저장
for _ in range(N):
    board_data.append(input().strip())

chess_board = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']

ans = 64
for y in range(N-7):
    for x in range(M-7):
        change_color = 64 - paint_count(board_data, x, y)  # 다시 칠해야 하는 정사각형의 개수
        if ans > change_color:
            ans = change_color
        if ans == 0:  # 0보다 작아질 수는 없기때문에 탐색 종료조건으로 추가
            break

print(ans)