import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
B = []
for _ in range(M):
    B.append(list(map(int, input().split())))

AB = []
for i in range(N):
    values = []
    for j in range(K):
        value = 0
        for k in range(M):
            value += A[i][k] * B[k][j]
        values.append(value)
    AB.append(values)

for i in range(N):
    for j in range(K):
        print(AB[i][j], end=' ')
    print()