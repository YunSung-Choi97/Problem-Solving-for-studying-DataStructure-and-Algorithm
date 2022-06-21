import sys
input = sys.stdin.readline

T = int(input())  # 테스트 케이스의 개수

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())  # 출발점과 도착점의 좌표
    n = int(input())  # 행성계의 개수
    count = 0
    for planet in range(n):
        cx, cy, r = map(int, input().split())  # 행성계 중심의 좌표와 반지름
        # 원의 방정식 (x - cx)^2 + (y - cy)^2 = r^2 을 이용해 점이 원의 내부/외부에 있는지 확인
        # 한 점은 내부, 한 점은 외부에 있는 경우에 행성계 진입/이탈이 발생
        if ((x1 - cx)**2 + (y1 - cy)**2 - r**2) * ((x2 - cx)**2 + (y2 - cy)**2 - r**2) < 0:
            count += 1
    print(count)