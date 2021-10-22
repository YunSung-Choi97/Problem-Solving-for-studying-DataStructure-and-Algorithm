import sys
input = sys.stdin.readline

# N번째 계단을 가는 법 : (N-2)번째 계단에서 오는 법, (N-1)번째 계단에서 오는 법
def get_score(n):
    dp[n] = max(dp[n - 2] + data[n], dp[n - 3] + data[n - 1] + data[n])
    return dp[n]

# 입력받기
N = int(input())
data = [0]
for i in range(N):
    data.append(int(input()))

# N이 1 또는 2인 경우는 계단 모두 사용
if N == 1:
    print(data[1])
elif N == 2:
    print(data[1] + data[2])
# N이 3 이상인 경우 get_score()함수 이용
else:
    # dp 초기화
    dp = [0] * (N + 1)
    dp[1] = data[1]
    dp[2] = data[1] + data[2]

    # dp 계산
    for i in range(3, N + 1):
        get_score(i)
    
    # 정답 출력
    print(dp[N])