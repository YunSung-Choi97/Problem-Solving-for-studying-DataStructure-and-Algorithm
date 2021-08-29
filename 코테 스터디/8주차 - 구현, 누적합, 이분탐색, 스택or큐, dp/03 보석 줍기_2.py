import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = []
sum_data = []
value_sum = 0
for _ in range(N):
    value = int(input())
    data.append(value)
    value_sum += value
    sum_data.append(value_sum)


sum_max_data = [0 for _ in range(N)]
temp = sum_data[N-1]
for i in range(N):
    if temp < sum_data[N-(i+1)]:
        temp = sum_data[N-(i+1)]
    sum_max_data[-(i+1)] = temp


sum_min_data = [0 for _ in range(N)]
temp = sum_data[0]
for i in range(N):
    if temp > sum_data[i]:
        temp = sum_data[i]
    sum_min_data[i] = temp


answer = []
answer.append(sum_max_data[M-1])
for i in range(1, N-M+1):
    answer.append(sum_max_data[M-1+i] - sum_min_data[i-1])


print('{:13}'.format('data'), data)
print('{:13}'.format('sum_data'), sum_data)
print('{:13}'.format('sum_max_data'), sum_max_data)
print('{:13}'.format('sum_min_data'), sum_min_data)
print('{:13}'.format('answer'), answer)

print(max(answer))