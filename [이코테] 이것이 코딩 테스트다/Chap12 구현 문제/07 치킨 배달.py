from itertools import combinations

N, M = map(int, input().split())  # 도시의 크기, 남겨질 치킨 집 개수
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))  # 도시 정보 저장

# 치킨 집 위치와 집 위치 정보를 따로 저장
house_map = []
chicken_map = []
for r in range(N):
    for c in range(N):
        if graph[r][c] == 1:
            house_map.append((r, c))
        elif graph[r][c] == 2:
            chicken_map.append((r, c))

result = 100 * 100  # 결과: 가능한 도시의 치킨 거리보다 큰 수로 초기화 (최대 거리 x 최대 개수)
for new_chicken_map in combinations(chicken_map, M):
    distance_of_city = 0  # 도시의 치킨 거리
    for house in house_map:
        distance = 100  # 치킨 거리: 가능한 치킨 거리보다 큰 수로 초기화
        for chicken in new_chicken_map:
            distance = min(distance, abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))
        distance_of_city += distance
    result = min(result, distance_of_city)

# 결과 출력
print(result)

''' 입력 예시 1
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
'''
''' 출력 예시 1
5
'''

''' 입력 예시 2
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
'''
''' 출력 예시 2
10
'''

''' 입력 예시 3
5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
'''
''' 출력 예시 3
11
'''

''' 입력 예시 4
5 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
'''
''' 출력 예시 4
32
'''