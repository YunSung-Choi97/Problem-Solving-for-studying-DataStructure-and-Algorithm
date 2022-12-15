from collections import deque

n = int(input())  # 수강할 강의 수

lecture_time = [0]  # 강의 시간
graph = [[] for _ in range(n + 1)]  # 과목 이수체계 (i번 과목을 선수과목으로 하는 과목들 graph[i]에 추가)
indegree = [0] * (n + 1)  # 수강하지 않은 선수과목 수
study = deque()  # 공부할 과목번호

for i in range(1, n + 1):
    lecture = list(map(int, input().split()))  # 강의 시간, 선수 과목 번호들, 종결자(-1)

    lecture_time.append(lecture[0])  # 강의 시간 저장

    for j in lecture[1:-1]:
        graph[j].append(i)  # 과목 이수 체계 j > i
        indegree[i] += 1  # i를 듣기 전 들어야할 과목 추가
    # 먼저 공부할 과목이 없는 경우
    if indegree[i] == 0:
        study.append(i)  # 공부할 과목에 추가

min_time = [0] * (n + 1)  # 과목을 수강하기 위한 최소한의 시간
while study:
    # 현재 수강 과목 처리
    now = study.popleft()
    min_time[now] += lecture_time[now]
    # 현재 과목을 선수과목으로 하는 과목 처리
    for next in graph[now]:
        min_time[next] = max(min_time[next], min_time[now])  # 다음 과목은 선수 과목들의 수강 시간 중 최대값을 최소한으로 필요함
        indegree[next] -= 1  # 선수 과목 하나 이수처리
        # 다음 과목이 선수 과목을 모두 수강한 경우
        if indegree[next] == 0:
            study.append(next)  # 공부 목록에 추가

# 결과 출력
for i in range(1, n + 1):
    print(min_time[i])
        
''' 입력 예시 1
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''
''' 출력 예시 1
10
20
14
18
17
'''