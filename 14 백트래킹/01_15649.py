N, M = map(int, input().split())

answer = []
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

''' itertools의 permutations를 호출해 순열을 만들어 출력
from itertools import permutations

N, M = map(int, input().split())

answers = permutations(range(1, N+1), M)  # nPm
for answer in answers:
    for num in answer:
        print(num, end=' ')
    print()
'''