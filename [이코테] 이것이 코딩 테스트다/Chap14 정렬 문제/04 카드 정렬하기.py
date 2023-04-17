from queue import PriorityQueue

N = int(input())  # 카드 묶음의 수
deck_size = PriorityQueue()
for _ in range(N):
    deck_size.put(int(input()))

answer = 0  # 비교 횟수
while True:
    # 하나의 카드 묶음으로 만든 경우 비교 종료
    if deck_size.qsize() == 1:
        break
    # 가장 작은 두 개의 카드 묶음을 합친 후 저장
    count = deck_size.get() + deck_size.get()
    answer += count
    deck_size.put(count)

# 결과 출력
print(answer)

''' 입력 예시 1
3
10
20
40
'''
''' 출력 예시 1
100
'''