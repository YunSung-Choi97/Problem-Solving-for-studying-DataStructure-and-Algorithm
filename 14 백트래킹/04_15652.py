N, M = map(int, input().split())

answer = []
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

''' itertools의 combinations를 호출해 중복있는 조합을 만들어 출력
from itertools import combinations_with_replacement

N, M = map(int, input().split())
answers = combinations_with_replacement(range(1, N+1), M)  # 중복있는 조합

for answer in answers:
    for num in answer:
        print(num, end=' ')
    print()
'''