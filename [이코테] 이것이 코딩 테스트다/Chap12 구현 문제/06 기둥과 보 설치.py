def check_beam(n, pillar, beam, x, y):
    # 보의 왼쪽 아래에 기둥 확인
    if y - 1 >= 0 and pillar[y - 1][x]:
        return True
    # 보의 오른쪽 아래에 기둥 확인
    if y - 1 >= 0 and x + 1 <= n and pillar[y - 1][x + 1]:
        return True
    # 보의 양쪽 끝 부분에 다른 보 확인
    if x - 1 >= 0 and x + 1 <= n and beam[y][x - 1] and beam[y][x + 1]:
        return True
    return False

def check_pillar(n, pillar, beam, x, y):
    # 바닥 위인지 확인
    if y == 0:
        return True
    # 보의 왼쪽 위인지 확인
    if beam[y][x]:
        return True
    # 보의 오른쪽 위인지 확인
    if x - 1 >= 0 and beam[y][x - 1]:
        return True
    # 다른 기둥 위인지 확인
    if y - 1 >= 0 and pillar[y - 1][x]:
        return True
    return False

def build(n, pillar, beam, x, y, a, b):
    if a == 1 and b == 1:  # 보 설치
        if check_beam(n, pillar, beam, x, y):
            beam[y][x] = True
    elif a == 0 and b == 1:  # 기둥 설치
        if check_pillar(n, pillar, beam, x, y):
            pillar[y][x] = True
    elif a == 1 and b == 0:  # 보 삭제
        beam[y][x] = False
        # 왼쪽에 연결된 보 확인
        if x - 1 >= 0 and beam[y][x - 1] and check_beam(n, pillar, beam, x - 1, y) == False:
            beam[y][x] = True
        # 오른쪽에 연결된 보 확인
        if x + 1 <= n and beam[y][x + 1] and check_beam(n, pillar, beam, x + 1, y) == False:
            beam[y][x] = True
        # 왼쪽에 올려진 기둥 확인
        if pillar[y][x] and check_pillar(n, pillar, beam, x, y) == False:
            beam[y][x] = True
        # 오른쪽에 올려진 기둥 확인
        if x + 1 <= n and pillar[y][x + 1] and check_pillar(n, pillar, beam, x + 1, y) == False:
            beam[y][x] = True
    else:  # 기둥 삭제
        pillar[y][x] = False
        # 기둥 위 왼쪽으로 연결된 보 확인
        if x - 1 >= 0 and y + 1 <= n and beam[y + 1][x - 1] and check_beam(n, pillar, beam, x - 1, y + 1) == False:
            pillar[y][x] = True
        # 기둥 위 오른쪽으로 연결된 보 확인
        if y + 1 <= n and beam[y + 1][x] and check_beam(n, pillar, beam, x, y + 1) == False:
            pillar[y][x] = True
        # 기둥 위 올려진 기둥 확인
        if y + 1 <= n and pillar[y + 1][x] and check_pillar(n, pillar, beam, x, y + 1) == False:
            pillar[y][x] = True

def print_result(n, pillar, beam):
    print('pillar')
    for i in range(n, -1, -1):
        print(pillar[i])
    print('beam')
    for i in range(n, -1, -1):
        print(beam[i])
    print()

def solution(n, build_frame):
    pillar = [[False] * (n + 1) for _ in range(n + 1)]  # 건설된 기둥
    beam = [[False] * (n + 1) for _ in range(n + 1)]  # 건설된 보
    for i in range(len(build_frame)):
        x, y, a, b = build_frame[i]  # x좌표, y좌표, 보/기둥, 설치/삭제
        build(n, pillar, beam, x, y, a, b)
    
    # 최종 건축물 저장
    answer = []
    for x in range(n + 1):
        for y in range(n + 1):
            if pillar[y][x]:
                answer.append([x, y, 0])
            if beam[y][x]:
                answer.append([x, y, 1])
    
    return answer

''' 입력 예시 1
5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
'''
''' 출력 예시 1
[[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
'''

''' 입력 예시 2
5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
'''
''' 출력 예시 2
[[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
'''