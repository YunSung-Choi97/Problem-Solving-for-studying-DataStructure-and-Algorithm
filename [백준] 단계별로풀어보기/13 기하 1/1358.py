import sys
input = sys.stdin.readline

w, h, x, y, p = map(int, input().split())  # 링크장 위치정보, 가로길이, 세로길이, 인원수 정보 입력받기
result = 0  # 링크장 내부 또는 경계에 있는 사람의 수
for _ in range(p):
    px, py = map(int, input().split())
    # 하키 링크의 직사각형 부분에 있는 경우
    if x <= px <= x + w and y <= py <= y + h:
        result += 1
    # 하키 링크의 왼쪽 반원 부분에 있는 경우
    elif (px - x)**2 + (py - (y + 0.5*h))**2 <= (0.5*h)**2:
        result += 1
    # 하키 링크의 오른쪽 반원 부분에 있는 경우
    elif (px - (x + w))**2 + (py - (y + 0.5*h))**2 <= (0.5*h)**2:
        result += 1

# 결과 출력
print(result)