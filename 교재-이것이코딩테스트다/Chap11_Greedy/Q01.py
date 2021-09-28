import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
data.sort()

groups = []
group = []

for i in data:
    if len(group) == 0:
        group.append(i)
    elif group[-1] > len(group):
        group.append(i)
    else:
        groups.append(group)
        group = []

print(len(groups))    