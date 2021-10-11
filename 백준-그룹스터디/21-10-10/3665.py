import sys
from collections import deque
input = sys.stdin.readline

# 위상정렬
def topology_sort():
    result = []
    queue = deque()

    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)
    
    # 큐가 빌 때까지
    while queue:
        now = queue.popleft()
        result.append(now)

        # 연결된 노드들 진입차수 -1
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    
    return result

T = int(input())
for _ in range(T):  # Test case만큼 반복
    # 팀 수, 작년 순위 저장
    n = int(input())
    last_rank = list(map(int, input().split()))
    
    # 그래프, 진입차수 저장
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    for i in range(n):
        for j in range(i+1, n):
            graph[last_rank[i]].append(last_rank[j])
            indegree[last_rank[j]] += 1
    
    # 변동사항 적용
    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        if b in graph[a]:
            graph[a].remove(b)
            indegree[b] -= 1
            graph[b].append(a)
            indegree[a] += 1
        else:
            graph[b].remove(a)
            indegree[a] -= 1
            graph[a].append(b)
            indegree[b] += 1
    
    # 위상정렬 수행
    answer = topology_sort()

    if len(answer) == n:  # 모든 팀의 순위가 올바르게 정렬된 경우
        print(*answer)
    else:  # 모든 팀의 순위가 올바르게 나열되지 못한 경우
        print('IMPOSSIBLE')