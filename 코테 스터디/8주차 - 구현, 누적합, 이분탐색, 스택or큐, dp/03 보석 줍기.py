import sys
input = sys.stdin.readline

N, M = map(int, input().split())

data = []  # 입력받은 보석의 가치 저장
sum_data = []  # 0 ~ index 까지의 보석 가치의 합
value_sum = 0
for _ in range(N):
    value = int(input())
    data.append(value)
    value_sum += value
    sum_data.append(value_sum)

max_data = [0 for _ in range(N-M+1)]  # sum_data의 index ~ end 중 최대값.  즉, 0 ~ index(+???) 까지의 보석 가치의 합 (??? 는 최대가 되게 하는 수)
temp = sum_data[N-1]
for i in range(N-M+1):
    if temp < sum_data[N-(i+1)]:
        temp = sum_data[N-(i+1)]
    max_data[-(i+1)] = temp

answer = []
answer.append(max_data[0])  # max_data에서 앞에서부터 하나씩 보석을 빼며 최대값을 구해봄
for i in range(1, N-M+1):
    answer.append(max_data[i] - sum_data[i-1])

if max(answer) < 0:
    print(0)
else:
    print(max(answer))