# 금광에서 채굴자가 얻을 수 있는 금의 최대 크기를 출력
def solution():
    N, M = map(int, input().split())  # 행의 개수, 열의 개수
    gold = list(map(int, input().split()))  # 금의 개수

    board = [gold[M * y:M * (y + 1)].copy() for y in range(N)]  # 위치별 금의 개수
    
    dp = [[0 for x in range(M)] for y in range(N)]  # 위치별 최대 채굴 금의 개수

    # 시작 지점 금의 개수 할당
    for y in range(N):
        dp[y][0] = board[y][0]
    
    # 열을 오른쪽으로 이동하며 최대 채굴 금의 개수 업데이트
    dy = [-1, 0, 1]  # 세로 축 이동
    for x in range(1, M):
        for y in range(N):
            previous = 0  # 현재 위치로 올 수 있는 이전 위치 중 최대 채굴 금의 개수
            for d in range(3):
                px, py = x - 1, y + dy[d]
                # 금광이 아닌 경우 통과
                if not (0 <= py < N):
                    continue
                previous = max(previous, dp[py][px])
            dp[y][x] = previous + board[y][x]
    
    # 결과 확인
    result = 0
    for y in range(N):
        result = max(result, dp[y][-1])
    
    print(result)  # 결과 출력

T = int(input())  # 테스트 케이스의 개수

# 테스트 케이스만큼 문제 해결 실행
for _ in range(T):
    solution()

''' 입력 예시 1
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
'''
''' 출력 예시 1
19
16
'''