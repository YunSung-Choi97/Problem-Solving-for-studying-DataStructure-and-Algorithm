'''미리 생각하기
1. 입력받기 >> N x 6 크기의 2차원 리스트에 주사위 정보 저장
2. 1층 주사위 아랫면 결정 시 주사위 옆면 최대값 결정 가능
  >> 6가지 경우 확인
'''

import sys

# 입력받기
N = int(input())
data_set = []
for _ in range(N):
    A, B, C, D, E, F = map(int, sys.stdin.readline().split())
    data_set.append((A, B, C, F, D, E))  # 인덱스 +/- 3을 했을 때 반대면이 나오도록 인덱스 조정

result = []
# 1층의 아랫면 1 ~ 6까지 확인
for case in range(6):
    side = 6 * N  # 옆면들 중 한면의 최대값
    # 아랫면 선택 >> 윗면 선택
    underside = data_set[0][case]
    upperside = data_set[0][case+3] if case < 3 else data_set[0][case-3]

    # 옆면 감점
    if underside != 6 and upperside != 6:
        pass
    elif underside != 5 and upperside != 5:
        side -= 1
    else:
        side -= 2

    # 2층부터 꼭대기층까지 반복
    for layer in range(1, N):
        # 아랫면, 윗면 선택
        for i in range(6):
            if data_set[layer][i] == upperside:
                if i < 3:
                    underside, upperside = data_set[layer][i], data_set[layer][i+3]
                else:
                    underside, upperside = data_set[layer][i], data_set[layer][i-3]
                break
        
        # 옆면 감점
        if underside != 6 and upperside != 6:
            continue
        elif underside != 5 and upperside != 5:
            side -= 1
        else:
            side -= 2

    # 결과 저장
    result.append(side)

# 정답 출력
print(max(result))