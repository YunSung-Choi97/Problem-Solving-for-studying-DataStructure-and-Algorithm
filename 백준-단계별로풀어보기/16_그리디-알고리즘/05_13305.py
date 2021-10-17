import sys
input = sys.stdin.readline

N = int(input())  # 주유소의 개수
roads = list(map(int, input().split()))  # 도시간의 거리
costs = list(map(int, input().split()))  # 도시의 기름 가격

# 이전에 나온 도시의 기름 가격보다 저렴하지 않은 경우 이전에 나온 도시의 기름가격을 따라가도록 만듬
result = 0
cost = costs[0]
for i in range(N-1):
    costs[i] = min(cost, costs[i])
    cost = min(cost, costs[i])
    result += roads[i] * costs[i]

print(result)