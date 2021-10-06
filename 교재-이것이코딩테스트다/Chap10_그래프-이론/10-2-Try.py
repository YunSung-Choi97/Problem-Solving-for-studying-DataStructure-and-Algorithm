import sys
input = sys.stdin.readline

def union_team(a, b):
    if parent[a] == parent[b]:
        return
    if a < b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

def same_team(a, b):
    if parent[a] == parent[b]:
        return True
    else:
        return False

N, M = map(int, input().split())
parent = [i for i in range(N+1)]

for _ in range(M):
    task, a, b = map(int, input().split())
    if task == 0:
        union_team(a, b)
    elif task == 1:
        if same_team(a, b):
            print('YES')
        else:
            print('NO')