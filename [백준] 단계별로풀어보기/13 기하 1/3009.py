import sys
input = sys.stdin.readline

# 주어진 좌표의 x, y 값을 저장할 리스트
x_data = []
y_data = []

# 주어진 좌표의 x, y 값 저장
for _ in range(3):
    x, y = map(int, input().split())
    x_data.append(x)
    y_data.append(y)

# 한번만 등장한 x 좌표와 y 좌표 확인 후 출력
for i in range(3):
    if x_data.count(x_data[i]) == 1:
        x = x_data[i]
    if y_data.count(y_data[i]) == 1:
        y = y_data[i]
print(x, y)