N, M = map(int, input().split())

answer = []
def BT(k):
    # M개의 숫자를 선택
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    
    # k ~ N 중 하나의 숫자를 선택
    for i in range(k, N+1):
        if i in answer:  # 이미 고르지 않은 수를 선택
            continue
        answer.append(i)  # 선택한 수 추가
        BT(i+1)  # 선택범위 변경
        answer.pop()  # 선택한 수 제거

BT(1)

''' itertools의 combinations를 호출해 조합을 만들어 출력
from itertools import combinations

N, M = map(int, input().split())
answers = combinations(range(1, N+1), M)  # nCm

for answer in answers:
    for num in answer:
        print(num, end=' ')
    print()
'''