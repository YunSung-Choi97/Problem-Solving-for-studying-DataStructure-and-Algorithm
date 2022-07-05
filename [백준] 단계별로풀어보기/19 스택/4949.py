import sys
input = sys.stdin.readline

# 문자열 데이터 저장
strings = list()
while True:
    string = input().rstrip()
    if string == '.':
        break
    strings.append(string)

# 각 줄의 문자열이 균형을 이루고 있는지 확인
for string in strings:
    stack = list()
    result = True
    for char in string:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if len(stack) == 0:
                result = False
                break
            if stack.pop() != '(':
                result = False
                break
        elif char == '[':
            stack.append('[')
        elif char == ']':
            if len(stack) == 0:
                result = False
                break
            if stack.pop() != '[':
                result = False
                break
    if len(stack) != 0:
        result = False
    
    # 결과 출력
    if result:
        print('yes')
    else:
        print('no')