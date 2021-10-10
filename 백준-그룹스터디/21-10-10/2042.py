'''미리 생각하기
1. 입력받기
2. 
 2-1. k번째까지의 합산을 저장하는 리스트 생성
 2-2. i ~ k 사이의 합은 Sk - S(i-1)
'''

import sys
input = sys.stdin.readline

# 입력받기
N, M, K = map(int, input().split())
An, Sn = [0], [0]
for i in range(N):
    num = int(input())
    An.append(num)  # 인덱스에 맞는 숫자 저장
    Sn.append(Sn[-1] + num)  # 인덱스까지의 숫자 합계

change = dict()  # 변경된 값 저장
for _ in range(M+K):
    a, b, c = map(int, input().split())
    
    # 변경하기
    if a == 1:
        change_val = c - An[b]
        An[b] = c
        if change.get(b) == None:
            change[b] = change_val
        else:
            change[b] += change_val
            if change[b] == 0:
                del change[b]
    
    # 계산하여 출력하기
    elif a == 2:
        result = Sn[c] - Sn[b-1]
        for key in change.keys():
            if key < b or c < key:
                continue
            result += change[key]
        print(result)