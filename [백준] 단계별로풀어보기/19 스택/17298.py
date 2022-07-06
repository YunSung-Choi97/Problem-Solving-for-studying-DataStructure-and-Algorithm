import sys
input = sys.stdin.readline

# 문제정보 입력받기
N = int(input())
A = list(map(int, input().split()))

result = [-1] * N
i, j = 0, 0
while i < N:
    j += 1
    stack = list()
    if A[i] < A[j]:
        
