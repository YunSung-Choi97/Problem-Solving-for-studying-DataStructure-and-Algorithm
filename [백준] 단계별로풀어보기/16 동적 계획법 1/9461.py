import sys
input = sys.stdin.readline

dp = [0, 1, 1, 1, 2, 2, 3] + [0] * 94  # 이미 구한 P(N) 값을 저장하는 리스트

# P(N) 값을 구하는 함수
def P(n):
    if dp[n] != 0:
        return dp[n]
    
    dp[n] = P(n - 5) + P(n - 1)
    return dp[n]

T = int(input())
for _ in range(T):
    N = int(input())
    print(P(N))