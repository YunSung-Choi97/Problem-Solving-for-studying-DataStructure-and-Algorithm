from collections import deque

def solution(priorities, location):
    queue = deque()  # 프린트 사용을 위해 대기열
    for i in range(len(priorities)):
        queue.append((i, priorities[i]))
    
    p_sorted = sorted(priorities)  # 우선순위를 오름차순으로 정렬

    answer = 1
    while True:
        idx, p = queue.popleft()
        if p == p_sorted[-1]:  # 우선순위가 가장 큰 값인 경우
            if idx == location:
                return answer
            p_sorted.pop()  # 우선순위 최대값 pop
            answer += 1
        else:
            queue.append((idx, p))  # 아닌 경우 다시 큐에 push