import sys
input = sys.stdin.readline

# 회의 종료시간보다 늦게 시작하는 회의들만 반복하여 카운트
def greedy(meeting):
    cnt = 0
    start = 0
    for item in meeting:
        if item[0] >= start:
            start = item[1]
            cnt += 1
    return cnt

N = int(input())
meeting = []
for i in range(N):
    start, end = map(int, input().split())
    meeting.append((start, end))

# 회의 시작시간을 기준으로 정렬한 후 종료시간을 기준으로 재정렬
meeting = sorted(meeting, key = lambda item:item[0])
meeting = sorted(meeting, key = lambda item:item[1])

print(greedy(meeting))