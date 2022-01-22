import sys
from queue import PriorityQueue

# 입력받기 및 저장
input = sys.stdin.readline
N, M, K = map(int, input().split())
data = []
for _ in range(N):
    D, H = map(int, input().split())
    data.append((-D, -H))


# 화장실 이용 전 필요한 정보들
location = (K % M, K // M)  # 데카의 위치

new_data = [[] for _ in range(M)]  # M줄로 나누어 선 사원들의 정보를 갖는 리스트.  각각은 ((-D, -H), (x, y))
for i in range(N):
    new_data[i%M].append((data[i], (i%M, i//M)))

first_line = PriorityQueue()  # 선두 사원의 정보를 갖는 우선순위 큐
for i in range(M):
    if len(new_data[i]) != 0:
        first_line.put(new_data[i][0])


# 화장실 이용
for i in range(N):
    (x, y) = first_line.get()[1]  # 화장실 이용 사원의 위치 정보

    if (x, y) == location:  # 데카가 화장실은 이용한 경우
        print(i)
        break

    if y != len(new_data[x]) - 1:  # 화장실 이용 사원의 선두 변경
        first_line.put(new_data[x][y+1])