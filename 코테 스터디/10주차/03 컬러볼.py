import sys

N = int(input())
balls = []  # 각각 (공번호, 색, 크기)를 저장
for i in range(1, N+1):
    color, size = map(int, sys.stdin.readline().split())
    balls.append((i, color, size))

balls.sort(key=lambda x : x[2])  # 크기를 기준으로 정렬

total_sum = 0  # 현재 공보다 크기가 작은 공들의 크기 총합
color_sum = [0 for i in range(N+1)]  # (idx = 색상) 현재 공보다 크기가 작은 같은 색 공들의 크기 총합
answer = [0 for i in range(N+1)]  # (idx = 공번호) 전체 공 점수 - 같은 색 공 점수

j = 0
for i in range(N):
    while balls[j][2] < balls[i][2]:
        total_sum += balls[j][2]
        color_sum[balls[j][1]] += balls[j][2]
        j += 1
    answer[balls[i][0]] = total_sum - color_sum[balls[i][1]]

for i in range(1, N+1):
    print(answer[i])