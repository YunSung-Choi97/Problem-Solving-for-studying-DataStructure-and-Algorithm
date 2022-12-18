from collections import deque

n = int(input())  # 모험가 수
fear_data = list(map(int, input().split()))  # 공포도

# 공포도가 적은 사람부터 그룹을 만들기 위해 queue에 공포도 낮은 사람부터 삽입
fear_data.sort()
queue = deque()
for i in range(n):
    queue.append(fear_data[i])


groups = []  # 최종 모험가 그룹들
while queue:
    # 새로운 모험가 그룹, 그룹에서 가장 높은 공포도
    group = []
    max_fear = 1

    while queue and len(group) < max_fear:
        fear = queue.popleft()
        max_fear = max(max_fear, fear)
        group.append(fear)
    
    if len(group) >= max_fear:
        groups.append(group)

print(len(groups))  # 결과 출력

''' 입력 예시 1
5
2 3 1 2 2
'''
''' 출력 예시 1
2
'''