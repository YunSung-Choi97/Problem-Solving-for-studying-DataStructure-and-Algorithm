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


data_D = [[] for _ in range(M)]
data_H = [[] for _ in range(M)]
for i in range(len(data)):
    data_D[i%M].append(data[i][0])
    data_H[i%M].append(data[i][1])

first_line_D = dict()  # 선두 사원 줄번호(key) : 우선순위(value) 정보를 갖는 dict
first_line_H = dict()  # 선두 사원 줄번호(key) : 우선순위(value) 정보를 갖는 dict
for i in range(M):
    if len(data_D[i]) != 0:
        first_line_D[i] = data_D[i][0]
        first_line_H[i] = data_H[i][0]

num = [0 for i in range(M)]
INF = 1e6


# 화장실 이용
for i in range(N):
    D_idx = [key for key, value in first_line_D.items() if value == max(first_line_D.values())]
    if len(D_idx) == 1:
        idx = D_idx[0]
    else:
        H_max = -1
        for key in D_idx:
            if first_line_H[key] > H_max:
                H_max = first_line_H[key]
                idx = key
    debug = 0
    debug = 0

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
    if num[idx] >= len(data_D[idx]):
        first_line_D[idx] = -1
        first_line_H[idx] = -1
    else:
        first_line_D[idx] = data_D[idx][num[idx]]
        first_line_H[idx] = data_H[idx][num[idx]]