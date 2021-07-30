N = int(input())
data = list(map(int, input().split()))
data.sort()

groups = []
group = []

for i in data:
    if len(group) == 0:
        group.append(i)
        continue
    elif group[-1] > len(group):
        group.append(i)
        continue
    else:
        groups.append(group)
        group = []
        continue

# print(groups)
print(len(groups))    