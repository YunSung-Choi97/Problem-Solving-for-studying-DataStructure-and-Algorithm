import sys
input = sys.stdin.readline

# 입력받기 및 저장
N, M, K = map(int, input().split())
data = []
for _ in range(N):
    D, H = map(int, input().split())
    data.append((D, H))


new_data = [[] for _ in range(M)]  # new_data : M줄로 나눠선 줄 현황
for i in range(len(data)):
    new_data[i%M].append(data[i])

first_D = dict()  # 선두의 근무 일수
first_H = dict()  # 선두의 급한 정도
for i in range(M):
    if len(new_data[i]) != 0:
        first_D[i] = new_data[i][0][0]
        first_H[i] = new_data[i][0][1]

location = [K // M, K % M]  # 데카의 위치

search_idx_Dmax, search_idx_Hmax = True, True
count = 0
for _ in range(N):
    # 먼저 사용할 사원 위치 찾기
    if search_idx_Dmax:
        idx_Dmax = [key for key, value in first_D.items() if value == max(first_D.values())]
    if len(idx_Dmax) == 1:
        idx = idx_Dmax[0]
        case = 1
    
    else:
        if search_idx_Hmax:
            first_H_Dmax = {key : first_H[key] for key in idx_Dmax}
            idx_Hmax = [key for key, value in first_H_Dmax.items() if value == max(first_H_Dmax.values())]
        idx = idx_Hmax[0]
        if len(idx_Hmax) == 1:
            case = 2
        else:
            case = 3
    
    # 화장실 이용
    if idx == location[1]:  # 데카의 줄에 있는 사람이 화장실을 이용하는 경우
        count += 1
        if location[0] - count < 0:
            answer = _
            break
    
    del new_data[idx][0]

    if len(new_data[idx]) == 0:
        if case == 1:
            search_idx_Dmax, search_idx_Hmax = True, True
        elif case == 2:
            idx_Dmax.remove(idx)
            search_idx_Dmax, search_idx_Hmax = False, True
        elif case == 3:
            idx_Dmax.remove(idx)
            idx_Hmax.remove(idx)
            search_idx_Dmax, search_idx_Hmax = False, False
        del first_D[idx]
        del first_H[idx]
    else:
        if case == 1:
            if first_D[idx] <= new_data[idx][0][0]:
                search_idx_Dmax, search_idx_Hmax = False, False
            else:
                search_idx_Dmax, search_idx_Hmax = True, True
        elif case == 2 or case == 3:
            if first_D[idx] < new_data[idx][0][0]:
                idx_Dmax = [idx]
                search_idx_Dmax, search_idx_Hmax = False, False
            elif first_D[idx] == new_data[idx][0][0]:
                if first_H[idx] < new_data[idx][0][1]:
                    idx_Hmax = [idx]
                    search_idx_Dmax, search_idx_Hmax = False, False
                elif first_H[idx] == new_data[idx][0][1]:
                    search_idx_Dmax, search_idx_Hmax = False, False
                else:
                    if case == 2:
                        search_idx_Dmax, search_idx_Hmax = False, True
                    else:
                        idx_Hmax.remove(idx)
            else:
                search_idx_Dmax, search_idx_Hmax = True, True
        first_D[idx] = new_data[idx][0][0]
        first_H[idx] = new_data[idx][0][1]

print(answer)