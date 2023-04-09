# 두 "균형잡힌 괄호 문자열"을 반환
def get_balanced_string(string):
    open_bracket, close_bracket = 0, 0  # 여는 괄호 개수, 닫는 괄호 개수
    for i in range(len(string)):
        if string[i] == '(':
            open_bracket += 1
        else:
            close_bracket += 1
        # 두 균형잡힌 괄호 문자열로 구분하는 인덱스인 경우
        if open_bracket == close_bracket:
            u = string[:i + 1]
            v = string[i + 1:]
            break
    return [u, v]

# "올바른 괄호 문자열"인지 확인
def is_collect_string(string):
    stack = []
    for char in string:
        # 여는 괄호인 경우 stack에 저장
        if char == '(':
            stack.append(char)
        # 닫는 괄호인 경우
        else:
            # 여는 괄호를 가지고 있는 경우 나머지 확인
            if stack and stack.pop() == '(':
                continue
            # 여는 괄호를 가지고 있지 않은 경우 "올바른 괄호 문자열"이 아님
            else:
                return False
    return True

def solution(p):
    # (규칙1) 빈 문자열인 경우, 빈 문자열을 반환
    if p == '':
        return ''
    # (규칙2) 두 "균형잡힌 문자열"로 분리
    u, v = get_balanced_string(p)
    # (규칙3) u가 "올바른 괄호 문자열"인지 확인
    if is_collect_string(u):
        return u + solution(v)
    # (규칙4)
    else:
        # (규칙4-1)
        reverse_u = ''
        for char in u:
            if char == '(':
                reverse_u += ')'
            else:
                reverse_u += '('
        return '(' + solution(v) + ')' + reverse_u[1:-1]

# print(solution('(()())()'))
''' 입력 예시 1
'(()())()'
'''
''' 출력 예시 1
'(()())()'
'''

# print(solution(')('))
''' 입력 예시 2
')('
'''
''' 출력 예시 2
'()'
'''

# print(solution('()))((()'))
''' 입력 예시 3
'()))((()'
'''
''' 출력 예시 3
'()(())()'
'''