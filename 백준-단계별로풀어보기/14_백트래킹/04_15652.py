'''미리 생각하기 [Try 2]
1. 입력받기 (N, M)
2. 정답(출력할 줄)을 한 자리씩 선정하기 (BackTracking)
'''
# N, M 입력받기
N, M = map(int, input().split())

answer = []  # 출력할 정답을 저장할 공간
def BT(k):
    # M개의 숫자를 선택
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    
    # k ~ N 중 하나의 숫자를 선택
    for i in range(k, N+1):
        answer.append(i)  # 선택한 수 추가
        BT(i)  # 선택범위 변경
        answer.pop()  # 선택한 수 제거

BT(1)

'''미리 생각하기 [Try 1]
1. 주어진 정보 입력받기 (N, M)
2. itertools의 combinations_with_replacement를 이용
'''
''' itertools의 combinations를 호출해 중복있는 조합을 만들어 출력
from itertools import combinations_with_replacement

N, M = map(int, input().split())
answers = combinations_with_replacement(range(1, N+1), M)  # 중복있는 조합

for answer in answers:
    for num in answer:
        print(num, end=' ')
    print()
'''