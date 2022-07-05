import sys
input = sys.stdin.readline

T = int(input())  # 테스트 데이터의 수

for _ in range(T):
    PS = input().rstrip()  # 입력받은 괄호 문자열
    stack = list()
    VPS = True  # PS가 VPS인지 판단
    for i in range(len(PS)):
        if PS[i] == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                VPS = False
                break
            if stack.pop() == ')':
                VPS = False
                break
    if len(stack) != 0:
        VPS = False
    
    if VPS:
        print('YES')
    else:
        print('NO')