import sys
input = sys.stdin.readline

# 두 행렬의 곱을 계산하는 함수
def mul_matrix(X, Y, size):
    result = []
    for i in range(size):
        values = []
        for j in range(size):
            value = 0
            for k in range(size):
                value += X[i][k] * Y[k][j]
            value = value % 1000
            values.append(value)
        result.append(values)
    return result

# (main) A^B를 계산해주는 함수
# A^B 계산할 때
# B이 짝수라면 (A^(B//2))^2을 이용해 계산을 하고
# B이 홀수라면 (A^(B//2))^2*A를 이용해 계산을 해주었다.
def power_matrix(A, N, B):
    if B == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] = A[i][j] % 1000
        return A
    elif B == 2:
        return mul_matrix(A, A, N)
    elif B % 2 == 0:
        temp = power_matrix(A, N, B // 2)
        return mul_matrix(temp, temp, N)
    elif B % 2 == 1:
        temp = power_matrix(A, N, B // 2)
        squr = mul_matrix(temp, temp, N)
        return mul_matrix(squr, A, N)

N, B = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

answer = power_matrix(A, N, B)

for i in range(N):
    for j in range(N):
        print(answer[i][j], end=' ')
    print()