# 최적의 해를 구하는 순서를 출력하는 함수
def order(P, i, j):
    if i == j:
        print('A{}'.format(i), end='')
    else:
        k = P[i][j]
        print('(', end='')
        order(P, i, k)
        order(P, k+1, j)
        print(')', end='')

# 연쇄행렬 최소곱셈 알고리즘 구현
def minmult(size):
    for diagonal in range(1, size):
        for i in range(1, size - diagonal):
            j = i + diagonal
            M[i][j] = INF  # 계속해서 0으로 값이 할당되는 것을 막기 위해 매우 큰 수로 미리 할당
            for k in range(i, j):
                if M[i][j] > M[i][k] + M[k+1][j] + d[i-1]*d[k]*d[j]:
                    M[i][j] = M[i][k] + M[k+1][j] + d[i-1]*d[k]*d[j]
                    P[i][j] = k

# 행렬 출력 (한칸 : 4자리)
def printMatrix(matrix):
    R = len(matrix)
    C = len(matrix[0])
    for i in range(R):
        for j in range(C):
            print('{:4}'.format(matrix[i][j]),end=" ")
        print()

# Test case 1
d = [5, 2, 3, 4, 6, 7, 8]  # 행렬 각각의 크기

size = len(d)  # 행렬 개수 + 1
INF = int(1e8)  # min값을 구할 때 계속해서 0이 구해지는 것을 막기위한 무한값
M = [[0 for j in range(size)] for i in range(size)]
P = [[0 for j in range(size)] for i in range(size)]

# 연쇄행렬 최소곱셈 알고리즘 실행
minmult(size)

print('============ matrix M ============')
printMatrix(M)
print('\n============ matrix P ============')
printMatrix(P)
print('\n최적의 해를 구하기 위한 곱셈 순서 : ', end='')
order(P, 1, 6)