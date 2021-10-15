# 부분 서열에 대한 최적 맞춤 비용을 계산하는 함수
def opt(i, j):
    if i == m:
        return 2 * (n - j)
    if j == n:
        return 2 * (m - i)
    penalty = 0 if a[i] == b[j] else 1  # penalty 결정
    opt_val = min(opt(i + 1, j + 1) + penalty, opt(i + 1, j) + 2, opt(i, j + 1) + 2)  # 점화식 이용
    return opt_val

# 최적서열맞춤 찾아가기
def find_minindex(i, j):
    if table[i][j] == table[i][j + 1] + 2:
        minindex[i][j] = (i, j + 1)
        if j + 1 < n:
            find_minindex(i, j + 1)
    elif table[i][j] == table[i + 1][j] + 2:
        minindex[i][j] = (i + 1, j)
        if i + 1 < m:
            find_minindex(i + 1, j)
    else:
        minindex[i][j] = (i + 1, j + 1)
        if i + 1 < m and j + 1 < n:
            find_minindex(i + 1, j + 1)


# Test case 1
# a = ['A', 'A', 'C', 'A', 'G', 'T', 'T', 'A', 'C', 'C']
# b = ['T', 'A', 'A', 'G', 'G', 'T', 'C', 'A']

# Test case 2
a = ['C', 'A', 'C', 'A', 'T', 'T', 'A', 'C', 'C']
b = ['C', 'A', 'C', 'G', 'T', 'C', 'C', 'A']

m = len(a)
n = len(b)
table = [[0 for j in range(0, n + 1)] for i in range(0, m + 1)]
minindex = [[(0, 0) for j in range(0, n + 1)] for i in range(0, m + 1)]

for j in range(n - 1, -1, -1):
    table[m][j] = table[m][j + 1] + 2

for i in range(m - 1, -1, -1):
    table[i][n] = table[i + 1][n] + 2

# 대각선 방향으로 확인
for k in range(m - 1, -1, -1):
    i = k
    while i < m:
        j = (k + n - 1) - i
        if not (0 <= j < n):
            break
        table[i][j] = opt(i, j)
        i += 1
for k in range(n - 1, -1, -1):
    j = k
    while j >= 0:
        i = k - j
        if not (0 <= i < m):
            break
        table[i][j] = opt(i, j)
        j -= 1

# 경로에 따른 서열 맞춤
find_minindex(0, 0)

# table 출력
for row in table:
    for value in row:
        print('{:3}'.format(value), end=' ')
    print()

print()  # 줄바꿈으로 출력 구분

x, y = 0, 0
# 경로 출력
while (x < m and y < n):
    tx, ty = x, y
    print(minindex[x][y])
    (x, y)= minindex[x][y]
    if x == tx + 1 and y == ty + 1:
        print(a[tx], " ", b[ty])
    elif x == tx and y == ty + 1:
        print(" - ", " ", b[ty])
    else:
        print(a[tx], " " , " -")