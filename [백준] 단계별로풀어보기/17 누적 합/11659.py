import sys
input = sys.stdin.readline

# 문제정보 입력받기
N, M = map(int, input().split())
num_list = list(map(int, input().split()))

# 누적 합 계산
prefix_sum = [0, num_list[0]]
for i in range(1, N):
    prefix_sum.append(prefix_sum[i] + num_list[i])

# 결과 출력
for _ in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i - 1])