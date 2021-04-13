import sys
input = sys.stdin.readline

def nCr(n, r):
    if n-r < r:
        return nCr(n, n-r)
    elif r == 0:
        return 1
    elif r == 1:
        return n
    else:
        return nCr(n-1, r-1) + nCr(n-1, r)


N, K = map(int, input().split())

answer = nCr(N, K)
print(answer)