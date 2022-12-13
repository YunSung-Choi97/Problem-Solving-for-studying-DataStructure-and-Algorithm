import heapq

INF = int(1e9)

n, m, c = map(int, input().split())  # 도시 개수, 통로 개수, 메시지 출발 도시

graph = [[] for _ in range(n + 1)]  # 도시간 연결 통로
for _ in range(m):
    x, y, z = map(int, input().split())  # 출발지, 도착지, 소요 시간
    graph[x].append((y, z))

distance = [INF] * (n + 1)  # 도시까지 거리

def dijkstra(start):
    # 방문할 도시
    have_to_visit = []
    heapq.heappush(have_to_visit, (0, start))

    while have_to_visit:
        dist_now, now = heapq.heappop(have_to_visit)

        # 이미 방문한 도시
        if dist_now >= distance[now]:
            continue
        # 도시를 최단 경로로 방문
        distance[now] = dist_now
        for next, dist_now_to_next in graph[now]:
            dist_next = dist_now + dist_now_to_next
            if dist_next < distance[next]:  # 현재 도시까지 거리 + 현재 도시에서 다음 도시까지 거리 < 출발지에서 다음 도시까지 거리
                heapq.heappush(have_to_visit, (dist_next, next))

dijkstra(c)

# 결과 출력
count = 0
max_dist = 0
for dist in distance[1:]:
    if dist < INF:
        count += 1
        max_dist = max(dist, max_dist)
print(count - 1, max_dist)

''' 입력 예시 1
3 2 1
1 2 4
1 3 2
'''
''' 출력 예시 1
2 4
'''