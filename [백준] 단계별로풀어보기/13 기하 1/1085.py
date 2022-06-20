import sys
input = sys.stdin.readline

# 문제정보 입력받기
x, y, w, h = map(int, input().split())

# (x, y)에서 직사각형의 모든 경계선까지의 최소 거리
x_to_left = x
x_to_right = w - x
y_to_bottom = y
y_to_top = h - y

# 정답 출력
print(min(x_to_left, x_to_right, y_to_bottom, y_to_top))