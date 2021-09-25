'''미리 생각하기
1. 입력받기 >> 스도쿠 판을 9 x 9 크기의 2차원 리스트로 구현
2. 0의 위치 알아내기 << 데이터 입력받으며 함께 진행 가능
3. 0의 위치를 한칸씩 이동하며 가능한 수들을 넣어봄 (BackTracking)
'''
# Python3로는 시간초과가 발생하며, 이는 Pypy3로 통과할 수 있었다.

import sys

# 스도쿠 판의 정보 입력
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

# 스도쿠 판에서 0의 위치 저장
location = [(i, j) for i in range(9) for j in range(9) if graph[i][j] == 0]

# 위치 정보를 입력받아 그 위치에서 가능한 숫자들 반환
def possible_numbers(i, j):
    ret = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 가로 줄 확인
    for x in range(9):
        if graph[i][x] in ret:
            ret.remove(graph[i][x])
    # 세로 줄 확인
    for y in range(9):
        if graph[y][j] in ret:
            ret.remove(graph[y][j])
    # 3X3 박스 확인
    for y in range(i//3*3, i//3*3 + 3):
        for x in range(j//3*3, j//3*3+ 3):
            if graph[y][x] in ret:
                ret.remove(graph[y][x])
    
    return ret

# 스도쿠 구현
def sudoku(k):
    global flag

    if k == len(location):
        flag = True
        for row in graph:
            print(*row)
        return

    i, j = location[k][0], location[k][1]  # 채워넣어야할 스도쿠의 좌표
    possible_num = possible_numbers(i, j)  # 해당 좌표에 넣을 수 있는 수(들)
    for num in possible_num:
        graph[i][j] = num
        sudoku(k+1)
        if flag: return
        graph[i][j] = 0

flag = False
sudoku(0)  # 0번째 인덱스부터