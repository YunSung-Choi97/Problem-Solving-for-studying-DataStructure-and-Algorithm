import sys
input = sys.stdin.readline

# 문제정보 입력받기
N, K = map(int, input().split())
temperature_list = list(map(int, input().split()))

# 누적 합 계산
prefix_sum = [0]
for i in range(N):
    prefix_sum.append(prefix_sum[i] + temperature_list[i])

# 온도의 합 계산 및 결과 출력
result = list()
for i in range(N - K + 1):
    result.append(prefix_sum[i + K] - prefix_sum[i])
print(max(result))