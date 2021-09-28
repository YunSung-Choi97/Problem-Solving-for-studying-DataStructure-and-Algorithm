import sys
input = sys.stdin.readline

# N, M, K, 행렬데이터 입력받기
N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
B = []
for _ in range(M):
    B.append(list(map(int, input().split())))

# 행렬 곱셈 수행
# AB는 곱셈 결과.  AB = [values, valuse, ...], values = [value, value, ...]
AB = []
for i in range(N):
    values = []
    for j in range(K):
        value = 0
        for k in range(M):
            value += A[i][k] * B[k][j]
        values.append(value)
    AB.append(values)

# 결과 출력
for i in range(N):
    for j in range(K):
        print(AB[i][j], end=' ')
    print()