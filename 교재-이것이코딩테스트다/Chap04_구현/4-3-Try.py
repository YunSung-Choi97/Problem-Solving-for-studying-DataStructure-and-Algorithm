N, M = map(int, input().split())
y, x, d = map(int, input().split())
map_data = [list(map(int, input().split())) for i in range(N)]

map_data[y][x] = 2

while True:
    if map_data[y][x-1] != 0 and map_data[y][x+1] != 0 and map_data[y-1][x] != 0 and map_data[y+1][x] != 0:
        if d == 0:
            if map_data[y+1][x] != 1:
                y, x = y+1, x
            else:
                break
        elif d == 1:
            if map_data[y][x+1] != 1:
                y, x = y, x+1
            else:
                break
        elif d == 2:
            if map_data[y-1][x] != 1:
                y, x = y-1, x
            else:
                break
        elif d == 3:
            if map_data[y][x-1] != 1:
                y, x = y, x-1
            else:
                break

    if d == 0:
        if map_data[y][x-1] == 0:
            y, x, d = y, x-1, d+1
            map_data[y][x] = 2
        else:
            d = d+1
    elif d == 1:
        if map_data[y+1][x] == 0:
            y, x, d = y+1, x, d+1
            map_data[y][x] = 2
        else:
            d = d+1
    elif d == 2:
        if map_data[y][x+1] == 0:
            y, x, d = y, x+1, d+1
            map_data[y][x] = 2
        else:
            d = d+1
    elif d == 3:
        if map_data[y-1][x] == 0:
            y, x, d = y-1, x, d+1
            map_data[y][x] = 2
        else:
            d = d-3

count = 0
for i in range(N):
    for j in range(M):
        if map_data[i][j] == 2:
            count += 1

print(count)