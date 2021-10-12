import sys
input = sys.stdin.readline

# w(a, b, c)의 결과를 dp[a][b][c]에 저장
dp = [[[None for k in range(21)] for j in range(21)] for i in range(21)]
for i in range(1, 21):
    for j in range(1, 21):
        dp[0][i][j] = 1
        dp[i][0][j] = 1
        dp[i][j][0] = 1

# 문제의 w(a, b, c)구현. dp를 이용해 한번 계산된 값을 다시 계산하지 않도록 제작.
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        if dp[20][20][20] != None:
            return dp[20][20][20]
        else:
            dp[20][20][20] = w(20, 20, 20)
            return dp[20][20][20]
    if a < b and b < c:
        if dp[a][b][c] != None:
            return dp[a][b][c]
        else:
            dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
            return dp[a][b][c]
    if dp[a][b][c] != None:
        return dp[a][b][c]
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (-1, -1, -1):  # 종료조건
        break
    print('w({}, {}, {}) = {}'.format(a, b, c, w(a, b, c)))