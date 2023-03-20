import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    queue = deque()  # 방문할 도시
    queue.append(start)

    while queue:
        now = queue.popleft()
        if distance[now] > K:  # 찾는 도시보다 먼 도시인 경우
            return

        for city in roads[now]:
            if distance[city] == -1:  # 아직 방문하지 않은 도시
                if distance[now] + 1 == K:  # 찾는 도시인 경우
                    result.append(city)
                distance[city] = distance[now]  + 1  # 거리 저장
                queue.append(city)  # 방문할 도시에 추가

N, M, K, X = map(int, input().split())  # 도시의 개수, 도로의 개수, 찾아낼 거리, 출발 도시

roads = [[] for _ in range(N + 1)]  # 도로 정보 저장
for _ in range(M):
    start, end = map(int, input().split())
    roads[start].append(end)

distance = [-1] * (N + 1)  # 출발지로부터 거리
result = []  # 출발지로부터 거리가 K인 지점

# X에서부터 출발
distance[X] = 0
bfs(X)

# 결과 출력
result.sort()  # 결과 오름차순으로 정렬
if len(result) == 0:
    print(-1)
else:
    for city in result:
        print(city)

''' 입력 예시 1
4 4 2 1
1 2
1 3
2 3
2 4
'''
''' 출력 예시 1
4
'''

''' 입력 예시 2
4 3 2 1
1 2
1 3
1 4
'''
''' 출력 예시 2
-1
'''

''' 입력 예시 3
4 4 1 1
1 2
1 3
2 3
2 4
'''
''' 출력 예시 3
2
3
'''