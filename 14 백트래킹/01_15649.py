'''미리 생각하기 [Try 2]
1. 입력받기 (N, M)
2. 정답(출력할 줄)을 한 자리씩 선정하기 (BackTracking)
'''
# N, M 입력받기
N, M = map(int, input().split())

answer = []  # 출력할 정답을 저장할 공간
def BT():
    # M개의 숫자를 선택
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return

    # 1 ~ N 중 하나의 숫자를 선택
    for i in range(1, N + 1):
        if i in answer:  # 이미 고르지 않은 수를 선택
            continue
        answer.append(i)  # 선택한 수 추가
        BT()  # 반복
        answer.pop()  # 선택한 수 제거

BT()

'''미리 생각하기 [Try 1]
1. 주어진 정보 입력받기 (N, M)
2. itertools의 permutations를 이용
'''
''' itertools의 permutations를 호출해 순열을 만들어 출력
from itertools import permutations

N, M = map(int, input().split())

answers = permutations(range(1, N+1), M)  # nPm
for answer in answers:
    for num in answer:
        print(num, end=' ')
    print()
'''