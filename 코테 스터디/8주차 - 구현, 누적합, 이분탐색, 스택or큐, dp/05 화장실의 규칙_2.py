import sys
input = sys.stdin.readline

# 입력받기 및 저장
N, M, K = map(int, input().split())
data = []
for _ in range(N):
    D, H = map(int, input().split())
    data.append((D, H))

# 화장실 이용 전 필요한 정보들
location = (K % M, K // M)  # 데카의 위치
count = 0  # 데카와 같은 줄에서 화장실은 이용한 사원의 수

rank_data = sorted(sorted(list(set(data)), key=lambda x : x[1], reverse=True), reverse=True)  # 우선순위로 정렬한 정보

new_data = [[] for _ in range(M)]  # M줄로 나누어 선 사원들의 우선순위 정보
for i in range(len(data)):
    new_data[i%M].append(rank_data.index(data[i]))

first_line = dict()  # 선두 사원 줄번호(key) : 우선순위(value) 정보를 갖는 dict
for i in range(M):
    if len(new_data[i]) != 0:
        first_line[i] = new_data[i][0]

num = [0 for i in range(M)]
INF = 1e6

# 화장실 이용
for i in range(N):
    idx = min(first_line, key=first_line.get)  # 화장실 이용할 사원 선택.  idx : 우선순위가 가장 높은 사람의 줄 번호
    
    if idx == location[0]:  # 데카와 같은 줄 사람인지 확인
        count += 1
        if location[1] - count < 0:
            print(i)
            break
    
    # 화장실 이용한 사람은 줄에서 제거
    # del new_data[idx][0]
    # if len(new_data[idx]) == 0:
    #     del first_line[idx]
    # else:
    #     first_line[idx] = new_data[idx][0]
    num[idx] += 1
    if num[idx] == len(new_data[idx]):
        first_line[idx] = INF
    else:
        first_line[idx] = new_data[idx][num[idx]]
