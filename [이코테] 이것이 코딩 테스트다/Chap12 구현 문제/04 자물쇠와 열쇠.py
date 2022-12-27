def rotate_key(key):
    M = len(key)
    result = [[0] * M for _ in range(M)]
    for y in range(M):
        for x in range(M):
            result[y][x] = key[(M - 1) - x][y]
    return result

def try_open(key, lock, dx, dy):
    M = len(key)  # 열쇠 크기
    N = len(lock)  # 자물쇠 크기
    for y in range(N):
        for x in range(N):
            kx, ky = x - dx, y - dy
            # 자물쇠와 열쇠가 겹치는 부분인 경우
            if 0 <= kx < M and 0 <= ky < M:
                # (자물쇠 돌기 and 열쇠 홈) 또는 (자물쇠 홈 and 열쇠 돌기)가 아닌 경우 열 수 없음
                if not ((lock[y][x] == 1 and key[ky][kx] == 0) or (lock[y][x] == 0 and key[ky][kx] == 1)):
                    return False
            else:
                # 자물쇠가 돌기가 아닌 경우 열 수 없음
                if not (lock[y][x] == 1):
                    return False
    return True

def solution(key, lock):
    # 회전을 통해 만들 수 있는 열쇠 형태 저장
    keys = [key]
    for _ in range(3):
        keys.append(rotate_key(keys[-1]))

    M = len(key)  # 열쇠 크기
    N = len(lock)  # 자물쇠 크기
    for key in keys:  # 열쇠 회전
        for dy in range(-M - 1, N):  # 열쇠 y축 평행 이동
            for dx in range(-M - 1, N):  # 열쇠 x축 평행 이동
                if try_open(key, lock, dx, dy):  # 열쇠의 현재 회전 및 이동 상태에서 자물쇠와 비교
                    return True

    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

''' 입력 예시 1
[[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
'''
''' 출력 예시 1
True
'''