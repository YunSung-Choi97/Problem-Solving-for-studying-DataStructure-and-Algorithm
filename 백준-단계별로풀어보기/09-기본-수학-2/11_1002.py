import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    # 원의 중심 동일한 경우
    if x1 == x2 and y1 == y2:
        if r1 == r2:  # 원의 중심과 반지름 모두 동일
            print(-1)
        else:  # 원의 중심만 동일
            print(0)
    
    # 원의 중심이 다른 경우
    else:
        R = ((x2-x1)**2 + (y2-y1)**2)**0.5  # 원의 중심 사이의 거리

        # 큰 원 내부에 작은 원의 중심이 있는 경우
        if R < max(r1, r2) and R + min(r1, r2) < max(r1, r2):
            print(0)
        elif R < max(r1, r2) and R + min(r1, r2) == max(r1, r2):
            print(1)
        elif R < max(r1, r2) and R + min(r1, r2) > max(r1, r2):
            print(2)

        # 큰 원의 반지름 위에 작은 원의 중심이 있는 경우
        elif R == max(r1, r2):
            print(2)
            
        # 큰 원 외부에 작은 원의 중심이 있는 경우
        elif R > r1 + r2:
            print(0)
        elif R == r1 + r2:
            print(1)
        elif R < r1 + r2:
            print(2)