def dfs(graph, visited, start, del_node1, del_node2):
    # 이미 방문한 송전탑인 경우 검사X
    if visited[start]:
        return
    visited[start] = True  # 방문 처리
    # 현재 송전탑과 연결된 모든 전선을 확인
    for arrive in graph[start]:
        # 끊어진 전선은 이용하지 않도록 처리
        if start == del_node1 and arrive == del_node2:
            continue
        elif start == del_node2 and arrive == del_node1:
            continue
        # 전선 확인
        dfs(graph, visited, arrive, del_node1, del_node2)

def solution(n, wires):
    # 송전탑들의 연결 상태 정리 >> graph[출발탑] = [도착탑들...]
    graph = [[] for i in range(n+1)]  # 자연수이므로 0번 사용 X
    for i in range(n-1):
        graph[wires[i][0]].append(wires[i][1])
        graph[wires[i][1]].append(wires[i][0])

    result = n - 1  # 정답은 n - 1보다 작은 값이므로 임시 할당
    # 끊어진 전선의 두 송전탑을 바꿔가며 확인
    for del_node1, del_node2 in wires:
        visited = [False] * (n+1)
        start = wires[0][0]  # 검사시작할 송전탑
        if start == del_node1:
            start = wires[1][0]
        dfs(graph, visited, 1, del_node1, del_node2)
        
        count = visited.count(True)
        # |(방문한 송전탑 수) - (방문하지 못한 송전탑 수)| = |(count) = (n - count)|
        if result > abs(2 * count - n):
            result = abs(2 * count - n)
        
    return result


'''Test Case
n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
>>> 3

n = 4
wires = [[1,2],[2,3],[3,4]]
>>> 0

n = 7
wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]
>>> 1
'''

# print(solution(n, wires))