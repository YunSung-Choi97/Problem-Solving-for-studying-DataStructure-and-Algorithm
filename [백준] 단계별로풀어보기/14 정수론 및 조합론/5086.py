import sys
input = sys.stdin.readline

while True:
    num1, num2 = map(int, input().split())
    if num1 == 0 and num2 == 0:  # 종료 조건
        break

    if num1 % num2 == 0:    # num1이 num2의 배수
        print('multiple')
    elif num2 % num1 == 0:  # num1이 num2의 약수
        print('factor')
    else:                   # 배수/약수 관계가 아님
        print('neither')