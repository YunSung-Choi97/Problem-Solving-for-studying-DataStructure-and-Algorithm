# Node 정의
class Node:
    def __init__(self, data):
        self.l_child = None
        self.r_child = None
        self.data = data

# tree 정의
def tree(key, r, i, j):
    k = r[i][j]
    if (k == 0):
        return
    else:
        p = Node(key[k])
        p.l_child = tree(key, r, i, k - 1)
        p.r_child = tree(key, r, k + 1, j)
        return p

# 최적 이진 실행 트리 구현
def optsearchtree():
    for diagonal in range(1, n):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal
            # minimum 탐색을 시작하는 i번째를 기준으로 minimum과 minimum_idx 초기화
            minimum = a[i][i - 1] + a[i + 1][j]
            minimum_idx = i
            sum_p = 0  # 시그마 p값을 저장할 변수
            for k in range(i, j + 1):  # minimum과 minimum_idx 탐색, 시그마 p 계산
                temp = a[i][k - 1] + a[k + 1][j]
                if minimum > temp:
                    minimum = temp
                    minimum_idx = k
                sum_p += p[k]
            a[i][j] = minimum + sum_p
            r[i][j] = minimum_idx

# 주어진 utility모듈의 print_inOrder함수 사용
def print_inOrder(root):
    if not root:
        return
    print_inOrder(root.l_child)
    print(root.data)
    print_inOrder(root.r_child)

# 주어진 utility모듈의 print_preOrder함수 사용
def print_preOrder(root):
    if not root:
        return
    print(root.data)
    print_preOrder(root.l_child)
    print_preOrder(root.r_child)


# Test case 1
# key = [" ", "A", "B", "C", "D"]
# p = [0, 0.375, 0.375, 0.125, 0.125]


# # Test case 2
key = [" ", "A", "B", "C", "D", "E"]
p = [0, 3/15, 1/15, 2/15, 5/15, 4/15]

n = len(p) - 1
a = [[0 for j in range(0, n + 2)] for i in range(0, n + 2)]
r = [[0 for j in range(0, n + 2)] for i in range(0, n + 2)]
for i in range (1, n + 1):
    a[i][i - 1] = 0
    a[i][i] = p[i]
    r[i][i] = i
    r[i][i - 1] = 0
a[n + 1][n] = 0
r[n + 1][n] = 0

# 최적 이진 검색 트리 실행
optsearchtree()

# matrix A 출력
for row in a:
    for value in row:
        print('{:.2f}'.format(value), end=' ')
    print()

print()  # 줄바꿈으로 결과 구분

# matrix R 출력
for row in r:
    for value in row:
        print(value, end=' ')
    print()

print()

root = tree(key, r, 1, n)

print_inOrder(root)  # 주어진 utility모듈의 함수 사용

print()

print_preOrder(root)  # 주어진 utility모듈의 함수 사용