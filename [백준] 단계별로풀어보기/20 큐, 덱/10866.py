import sys
from collections import deque
input = sys.stdin.readline

N = int(input())  # 명령의 수

Deque = deque()
for _ in range(N):
    order = input().rstrip()

    if order[:10] == 'push_front':  # push front 명령
        Deque.appendleft(int(order[11:]))
    elif order[:9] == 'push_back':  # push back 명령
        Deque.append(int(order[10:]))
    elif order == 'pop_front':  # pop front 명령
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque.popleft())
    elif order == 'pop_back':  # push back 명령
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque.pop())
    elif order == 'size':  # size 명령
        print(len(Deque))
    elif order == 'empty':  # empty 명령
        if len(Deque) == 0:
            print(1)
        else:
            print(0)
    elif order == 'front':  # front 명령
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque[0])
    elif order == 'back':  # back 명령
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque[-1])