import sys

N = int(input())
data = []
for _ in range(N):
    name, score = sys.stdin.readline().split()
    data.append((name, score))

data.sort(key=lambda x:x[1])
for i in range(N):
    print(data[i][0])