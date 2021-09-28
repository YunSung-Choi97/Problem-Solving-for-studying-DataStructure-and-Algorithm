import sys

N = int(input())
data = list()
for _ in range(N):
    data.append(int(sys.stdin.readline()))

data.sort(reverse=True)
for num in data:
    print(num, end=' ')