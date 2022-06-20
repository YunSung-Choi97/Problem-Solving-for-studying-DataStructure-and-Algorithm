import sys
input = sys.stdin.readline

while True:
    # 삼각형 변의 길이 입력받기
    a, b, c = map(int, input().split())
    
    # 종료 조건
    if a == 0 and b == 0 and c == 0:
        break
    
    # 직각삼각형 판별
    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print("right")
    else:
        print("wrong")