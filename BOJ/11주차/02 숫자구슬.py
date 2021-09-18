import itertools
import sys

N, M = map(int, input().split())
data = list(map(int, input().split()))

if M == 1:
    print(sum(data))
    print(1)
    raise SystemExit

data_sum = list()
data_sum.append(data[0])
for i in range(1, N):
    data_sum.append(data_sum[i-1] + data[i])

idxs = list(itertools.combinations(range(1, N), M-1))
max_sum = data_sum[-1]
idx = None
length = len(idxs)

for i in range(length):
    result = []
    for j in range(M):
        if j == 0:
            value = data_sum[idxs[i][j]-1]
        elif j == M-1:
            value = data_sum[-1] - data_sum[idxs[i][-1]-1]
        else:
            value = data_sum[idxs[i][j]-1] - data_sum[idxs[i][j-1]-1]
        result.append(value)
    temp = max(result)
    if temp < max_sum:
        max_sum = temp
        idx = i

print(max_sum)
for i in range(M):
    if i == 0:
        print(idxs[idx][0], end=' ')
    elif i == M-1:
        print(N - idxs[idx][-1], end=' ')
    else:
        print(idxs[idx][i] - idxs[idx][i-1], end=' ')