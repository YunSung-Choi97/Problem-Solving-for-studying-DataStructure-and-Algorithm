import sys
input = sys.stdin.readline
from collections import deque

N = int(input())  # 명령의 수

queue = deque()
# 명령을 처리하는 프로그램
for _ in range(N):
    order = input().rstrip()

    if order == 'pop':  # pop 명령
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
    elif order == 'size':  # size 명령
        print(len(queue))
    elif order == 'empty':  # empty 명령
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order == 'front':  # front 명령
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif order == 'back':  # back 명령
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)        
    else:  # push 명령
        queue.append(int(order[5:]))