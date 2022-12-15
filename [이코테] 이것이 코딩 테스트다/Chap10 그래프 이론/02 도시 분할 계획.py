n, m = map(int, input().split())  # 마을 개수, 현재 길 개수

graph = []  # 현재 길 정보
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b))

graph.sort()  # 유지비를 기준으로 길 정렬

city = [i for i in range(n + 1)]  # 연결된 가장 상위 도시

# 도시 합치기
def union_city(a, b):
    # 이미 같은 도시인 경우 종료
    if city[a] == city[b]:
        return
    # b를 a도시로 합치기
    city[b] = city[a]

# 가장 상위 도시 찾기
def find_city(a):
    if city[a] != a:
        city[a] = find_city(city[a])
    return city[a]

# 연결된 도시인지 확인하기
def linked_city(a, b):
    cityA = find_city(a)
    cityB = find_city(b)
    if cityA == cityB:
        return True
    else:
        return False

total_cost = 0
last_cost = 0
for i in range(m):
    cost, a, b = graph[i]
    # 이미 연결된 도시
    if linked_city(a, b):
        continue
    union_city(a, b)  # 도시 연결
    total_cost += cost  # 길 유지비 추가
    last_cost = cost  # 마지막에 분리된 두 도시를 연결하는 길 유지비

# 두 도시를 연결하지 않도록 마지막 길 유지비를 제외한 결과 출력
print(total_cost - last_cost)

''' 입력 예시 1
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
'''
''' 출력 예시 1
8
'''