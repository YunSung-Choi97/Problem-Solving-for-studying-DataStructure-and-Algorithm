import sys
input = sys.stdin.readline

N = int(input())  # 명령의 수

stack = list()
# 명령을 처리하는 프로그램
for _ in range(N):
    order = input().rstrip()

    if order == 'pop':  # pop 명령
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif order == 'size':  # size 명령
        print(len(stack))
    elif order == 'empty':  # empty 명령
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order == 'top':  # top 명령
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
    else:  # push 명령
        stack.append(int(order[5:]))