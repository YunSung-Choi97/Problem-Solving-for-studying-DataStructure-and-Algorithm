# input() 보다 sys.stdin.readline()이 빠르다
# 시간 복잡도가 커질수록 차이는 커지게 된다.

import sys  # sys 모듈을 불러옴

T = int(input())  # T : 테스트 케이스의 개수

for i in range(T):  # T번 반복
    n, m = map(int, sys.stdin.readline().split())  # n, m : 한 줄씩 문자열을 입력받아 공백, tab, 줄바꿈을 기준으로 나눠 할당
    print(n+m)