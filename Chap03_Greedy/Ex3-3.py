N, M = map(int, input().split())

min_list = []

for i in range(N):
    data = list(map(int, input().split()))
    min_list.append(min(data))

print(max(min_list))