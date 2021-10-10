'''미리 생각하기
1. 입력받기
2. 특정 시간에 놀이기구를 이용한 아이들 수를 구하는 함수
3. 이분 탐색으로 N을 넘지않는 가장 큰 시간을 구하여 결과 계산
'''

import sys

N, M = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

if N < M:  # 이용자 수보다 놀이기구가 많은 경우
    print(N)
else:
    target, left, right = 0, 0, 30 * N
    while left <= right:
        mid = (left + right) // 2
        # count : 현재까지 이용한 아이들 수
        count = 0
        for i in range(M):
            count += (mid-1) // data[i] + 1
        
        if count >= N:
            right = mid - 1
        else:
            left = mid + 1
            target = mid  # target : (이용자 수가 N보다 작은 가장 큰 수) + 1
    
    count = 0
    for i in range(M):
        count += (target-1) // data[i] + 1
    rest = N - count  # rest : 시간 (target - 1)에 줄에 남은사람 수
    
    for i in range(M):
        if target % data[i] == 0:  # 이용가능한 놀이기구
            rest -= 1
            if rest == 0:
                print(i + 1)  # (인덱스 + 1) 출력
                break