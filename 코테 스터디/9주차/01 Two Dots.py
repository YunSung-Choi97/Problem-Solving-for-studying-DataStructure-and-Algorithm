import sys
input = sys.stdin.readline

def find_cycle(x1, y1, x2, y2, color):
    if x1 > x2:
        find_cycle(x2, y1, x1, y2, color)
    else:
        for x in range(x1, x2+1):
            if data[y1][x] != color:
                return False
            if data[y2][x] != color:
                return False
        for y in range(y1, y2+1):
            if data[y][x1] != color:
                return False
            if data[y][x2] != color:
                return False
        
        return True

N, M = map(int, input().split())
data = [input().rstrip() for _ in range(N)]

color_data = ''
for i in range(N):
    color_data += data[i]
color_data = list(set(color_data))

location_data = [[] for _ in range(len(color_data))]
for n in range(N):
    for m in range(M):
        location_data[color_data.index(data[n][m])].append((m, n))

for idx, color in enumerate(color_data):
    length = len(location_data[idx])
    if length < 4:
        continue

    for i in range(length):
        for j in range(i+1, length):
            x1, y1 = location_data[idx][i]
            x2, y2 = location_data[idx][j]
            if x1 == x2 or y1 == y2:
                continue
            if find_cycle(x1, y1, x2, y2, color):
                print("Yes")
                sys.exit()

print("No")