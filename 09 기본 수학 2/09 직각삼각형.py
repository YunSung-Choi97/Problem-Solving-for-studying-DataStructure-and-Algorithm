import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    
    # 종료 조건
    if a == 0 and b == 0 and c == 0:
        break
    
    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:  # 직각삼각형의 조건
        print("right")
    else:
        print("wrong")