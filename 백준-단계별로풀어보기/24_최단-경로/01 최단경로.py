import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())  # V, E : 정점의 개수, 간선의 개수
start_V = int(input())  # start_V : 시작 정점의 번호

# 2개의 리스트에 대하여 인덱스값과 출발점을 동일하게 생각해주기 위해 0번째 인덱스는 사용하지않음.
graph = [[] for _ in range(V+1)]  # graph : 각 점에서 갈수있는 점들의 정보 저장
distance = [INF] * (V+1)  # distance : 최단거리. 최초에는 무한으로 초기화

for _ in range(E):  # 간선의 정보 입력받음
    u, v, w = map(int, input().split())  # u, v, w : u에서 v로 가는 가중치 w의 간선
    graph[u].append((v, w))

# 방문하지 않은 정점 중 가장 최단거리가 짧은 정점의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, V+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

# 다익스트라 알고리즘
def dijkstra(start):  # 시작 정점의 번호를 입력으로 받음
    q = []
    heapq.heappush(q, (0, start))  # 시작노드로 가기위한 최단 경로는 0으로 설정하여, 큐에 삽입
    distance[start] = 0

    while q:  # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)  # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        
        if distance[now] < dist:  # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            continue

        for i in graph[now]:  # 현재 노드와 연결된 다른 인접한 노드들을 확인
            cost = dist + i[1]

            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start_V)

for i in range(1, V+1):
    if distance[i] == INF:  # 가지 못하는 점은 INF에서 변하지 않음
        print("INF")
    else:
        print(distance[i])