import sys
input = sys.stdin.readline

x_data = []  # x 좌표 정보들을 저장
y_data = []  # y 좌표 정보들을 저장
for _ in range(3):
    x, y = map(int, input().split())
    x_data.append(x)
    y_data.append(y)

# x, y 좌표정보들 중 데이터 개수가 하나인 좌표를 찾기
for i in range(3):
    if x_data.count(x_data[i]) == 1:
        x = x_data[i]
    if y_data.count(y_data[i]) == 1:
        y = y_data[i]

print(x, y)