N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(K):
    A_idx = A.index(min(A))
    B_idx = B.index(max(B))
    A[A_idx], B[B_idx] = B[B_idx], A[A_idx]

print(sum(A))