N, E, W, S = (0, -1), (1, 0), (-1, 0), (0, 1)  # N, E, W, S로 이동가능
blocks = {'|' : (N, S), '-' : (E, W), '+' : (N, E, W, S), '1' : (S, E), '2' : (N, E), '3' : (N, W), '4' : (S, W)}  # 블록의 입구 정보

R, C = map(int, input().split())
graph = []
for y in range(R):
    data = list(input())
    graph.append(data)
    if 'M' in data:
        M = (data.index('M'), y)  # M의 좌표
    if 'Z' in data:
        Z = (data.index('Z'), y)  # Z의 좌표

# M 또는 Z 지점에서 어떤 방향으로 이동할지 확인
def start_dir(x, y):
    for dir in [N, E, W, S]:
        nx = x + dir[0]
        ny = y + dir[1]
        if nx < 0 or C <= nx or ny < 0 or R <= ny:
            continue
        block = graph[ny][nx]
        if block in ['.', 'M', 'Z']:
            continue
        if (-dir[0], -dir[1]) in blocks[block]:
            return dir

# 규칙에 따라 이동, 이동불가능한 지점에 도착하면 (좌표, 입구방향) 반환
def move(From, dir):
    x = From[0] + dir[0]
    y = From[1] + dir[1]
    INdir = -dir[0], -dir[1]
    block = graph[y][x]

    if block == '.':
        return ((x, y), INdir)

    if block in ['|', '-', '+']:
        return move((x, y), dir)
    if block in ['1', '2', '3', '4']:
        if INdir in [N, S]:
            OUTdir = blocks[block][1]
        else:
            OUTdir = blocks[block][0]
        return move((x, y), OUTdir)

# M에서 출발하여 이동하다 (멈춘 지점, 입구)
M_dir = start_dir(M[0], M[1])
ans_xy, ans_dir1 = move(M, M_dir)
# Z에서 출발하여 이동하다 (멈춘 지점, 입구)
Z_dir = start_dir(Z[0], Z[1])
ans_xy, ans_dir2 = move(Z, Z_dir)
# 정답칸이 원래 + 블록이었는지 확인
is_plus_block = True
for dir in [N, E, W, S]:
    nx = ans_xy[0] + dir[0]
    ny = ans_xy[1] + dir[1]
    if nx < 0 or C <= nx or ny < 0 or R <= ny:
        is_plus_block = False
        break
    if graph[ny][nx] == '.':
        is_plus_block = False
        break
    if (-dir[0], -dir[1]) not in blocks[graph[ny][nx]]:
        is_plus_block = False
        break

if is_plus_block:
    print(ans_xy[1]+1, ans_xy[0]+1, '+')
else:
    for key, value in blocks.items():
        if value == (ans_dir1, ans_dir2) or value == (ans_dir2, ans_dir1):
            print(ans_xy[1]+1, ans_xy[0]+1, key)