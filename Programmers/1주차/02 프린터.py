from collections import deque

def solution(priorities, location):
    queue = deque()
    for i in range(len(priorities)):
        queue.append((i, priorities[i]))
    
    p_sorted = sorted(priorities)

    answer = 1
    while True:
        idx, p = queue.popleft()
        if p == p_sorted[-1]:
            if idx == location:
                return answer
            p_sorted.pop()
            answer += 1
        else:
            queue.append((idx, p))