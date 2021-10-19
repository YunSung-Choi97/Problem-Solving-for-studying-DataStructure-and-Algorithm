import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# (N)! / ((N-K)! * K!)
answer = 1
for i in range(K):
    answer = answer * (N-i) // (i+1)

print(answer)