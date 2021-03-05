import sys
input = sys.stdin.readline

INF = int(1e9)  # INF : 초기에 최단 경로를 무한대로 설정해주기 위해 큰 숫자를 넣어줌
V, E = map(int, input().split())  # V, E : 정점의 개수, 간선의 개수
start_V = int(input())  # start_V : 시작 정점의 번호

# 3개의 리스트에 대하여 인덱스값과 출발점을 동일하게 생각해주기 위해 0번째 인덱스는 사용하지않음.
graph = [[] for _ in range(V+1)]  # graph : 각 점에서 갈수있는 점들의 정보 저장
visited = [False] * (V+1)  # visited : 방문한 점을 확인
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
    # 시작점의 최단거리는 0, 방문은 한 점으로 바꿔줌
    distance[start] = 0
    visited[start] = True

    # 시작점에서 바로 갈수있는 점들에 최단거리 할당
    for i in graph[start]:
        distance[i[0]] = i[1]
    
    # 시작점을 제외한 전체 V-1개의 점에 대해 반복
    for i in range(V-1):
        now = get_smallest_node()  # 현재 최단거리가 가장 작은 점부터 진행.
        visited[now] = True

        # 현재 점과 연결된 점들을 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start_V)

for i in range(1, V+1):
    if distance[i] == INF:  # 가지 못하는 점은 INF에서 변하지 않음
        print("INF")
    else:
        print(distance[i])
