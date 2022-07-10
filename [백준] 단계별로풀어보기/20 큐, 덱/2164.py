from collections import deque

N = int(input())  # 카드 수 입력받기

# Queue에 카드 저장
queue = deque()
for i in range(1, N + 1):
    queue.append(i)

# 마지막 남게 되는 카드 출력
if N == 1:
    print(1)
else:
    while True:
        queue.popleft()
        
        if len(queue) != 1:
            queue.append(queue.popleft())
        else:
            break
    print(queue.popleft())