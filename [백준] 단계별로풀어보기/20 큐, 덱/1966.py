import sys
from collections import deque
input = sys.stdin.readline

T = int(input())  # 테스트케이스 개수

# 프로그램 실행
for _ in range(T):
    N, M = map(int, input().split())  # N(문서의 개수), M(궁금한 문서 위치)
    importance = list(map(int, input().split()))  # 문서들의 중요도

    printer = deque(importance.copy())  # 프린터에 현재 대기중인 문서들의 중요도
    importance.sort()  # 프린터에 들어있는 중요도(오름차순)

    count = 1  # 출력될 문서의 순서
    rest = N  # 남은 문서의 수
    while printer:
        now = printer.popleft()
        if M == 0:  # 현재 문서가 궁금한 문서인 경우
            if now == importance[-1]:
                result = count
                break
            else:
                printer.append(now)
                M = rest - 1
                continue
        else:
            if now == importance[-1]:
                importance.pop()
                count += 1
                rest -= 1
            else:
                printer.append(now)
        M -= 1

    # 결과 출력
    print(result)