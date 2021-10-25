from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    boxes = [[False for x in range(50)] for y in range(50)]  # 직사각형 내부 영역
    outline = []  # 직사각형의 테두리 (내부 포함)

    # 직사각형 내부 확인
    for box in rectangle:
        x1, y1, x2, y2 = box
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        for x in range(x1, x2):
            for y in range(y1, y2):
                boxes[y][x] = True

    for line in boxes:
        for box in line:
            if box:
                print(1, end=' ')
            else:
                print(0, end=' ')
        print()

    flag = False
    for y in range(1, 51):
        for x in range(1, 51):
            if boxes[y][x]:
                start = (y, x)
                flag = True
            if flag: break
        if flag: break

    Q = deque()
    visited = [[False for x in range(50)] for y in range(50)]  # 방문한 사각형 영역
    
    Q.append(start)
    visited[start[0]][start[1]] = True
    
    dir = ((1, 0), (-1, 0), (0, 1), (0, -1))
    while Q:
        y, x = Q.popleft()

        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            if not (0 <= nx <= 50 and 0 <= ny <= 50):
                continue
            if boxes[ny][nx] and not visited[ny][nx]:
                Q.append((ny, nx))
                visited[ny][nx] = True
            elif not boxes[ny][nx]:
                if i == 0:
                    outline.append((ny, nx, ny + 1, nx))
                elif i == 1:
                    outline.append((y, x, y + 1, x))
                elif i == 2:
                    outline.append((ny, nx, ny, nx + 1))
                elif i == 3:
                    outline.append((y, x, y, x + 1))

    print(outline)
    print(len(outline))
        

    answer = 0
    return answer

rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
characterX = 1
characterY = 3
itemX = 7
itemY = 8
# result = 17

# rectangle = [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]
# characterX = 9
# characterY = 7
# itemX = 6
# itemY = 1
# # result = 11

# rectangle = [[1,1,5,7]]
# characterX = 1
# characterY = 1
# itemX = 4
# itemY = 7
# # result = 9

# rectangle = [[2,1,7,5],[6,4,10,10]]
# characterX = 3
# characterY = 1
# itemX = 7
# itemY = 10
# # result = 15

# rectangle = [[2,2,5,5],[1,3,6,4],[3,1,4,6]]
# characterX = 1
# characterY = 4
# itemX = 6
# itemY = 3
# # result = 10

solution(rectangle, characterX, characterY, itemX, itemY)