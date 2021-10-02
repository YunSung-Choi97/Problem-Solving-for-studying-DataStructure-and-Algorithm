'''미리 생각하기
1. 입력받기
 1-1. N, M
 1-2. N x M 크기의 2차원 리스트로 탐사 가치 저장
2. N x M 크기의 2차원 리스트에 탐사한 지역들의 가치의 최대값 저장
 2-1. left : (i, j) = max( (i-1, j), (i, j-1) ) , right : (i, j) = max( (i-1, j), (i, j-1) )
 2-2. 큰 값으로 한줄씩 완성
'''

import sys

# 입력받기
N, M = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# dp 테이블 초기화
dp = [[0 for i in range(M)] for j in range(N)]  # left와 right 중 큰 값 최종 선택
dp_left = [[0 for i in range(M)] for j in range(N)]  # 왼쪽에서 오는 값과 위에서 내려온 값 중 큰 값 선택
dp_right = [[0 for i in range(M)] for j in range(N)]  # 오른쪽에서 오는 값과 위에서 내려온 값 중 큰 값 선택
# 첫 줄은 오른쪽으로만 이동가능
dp[0][0], dp_left[0][0], dp_right[0][0] = graph[0][0], graph[0][0], graph[0][0]
for i in range(1, M):
    dp[0][i] = dp[0][i-1] + graph[0][i]
    dp_left[0][i] = dp[0][i-1] + graph[0][i]
    dp_right[0][i] = dp[0][i-1] + graph[0][i]

# 두 번째 줄 ~ 마지막 줄에 대하여 dp = max(left, right)
for y in range(1, N):
    # 첫 열과 마지막 열 값 초기화
    dp_left[y][0] = dp[y-1][0] + graph[y][0]
    dp_right[y][M-1] = dp[y-1][M-1] + graph[y][M-1]

    # left와 right 값 결정
    for x in range(1, M):
        dp_left[y][x] = max(dp_left[y][x-1] + graph[y][x], dp[y-1][x] + graph[y][x])
        dp_right[y][(M-1)-x] = max(dp_right[y][(M-1)-(x-1)] + graph[y][(M-1)-x], dp[y-1][(M-1)-x] + graph[y][(M-1)-x])
    
    # dp 값 결정
    for x in range(M):
        dp[y][x] = max(dp_left[y][x], dp_right[y][x])

# 정답 출력
print(dp[-1][-1])