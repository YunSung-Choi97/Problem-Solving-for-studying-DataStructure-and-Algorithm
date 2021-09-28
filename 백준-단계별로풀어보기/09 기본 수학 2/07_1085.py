import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

# (x, y)에서 직사각형의 경계선까지의 모든 거리
x_to_left = x
x_to_right = w - x
y_to_bottom = y
y_to_top = h - y

print(min(x_to_left, x_to_right, y_to_bottom, y_to_top))