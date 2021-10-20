import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    # (M)! / ((M-N)! * N!)
    answer = 1
    for i in range(N):
        answer = answer * (M-i) // (i+1)
    print(answer)