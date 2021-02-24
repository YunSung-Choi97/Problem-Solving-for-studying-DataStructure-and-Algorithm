while True:  # 무한루프 형성
    data = input()  # data : 입력받은 문자열을 할당
    if data == '.':  # 무한루프 종료조건
        break
    
    stk = []  # stk : 소괄호와 대괄호를 저장하는 stack공간 형성
    result = True  # result : 입력받은 문자열이 균형잡힌 문자열인지 판단. 아래의 조건을 통해 균형잡힌 문자열이 아니라면 False로 변환.

    for val in data:  # 입력받은 문자열을 한 글자씩 읽음
        
        # 여는 괄호일 경우 stk에 추가
        if val == '(' or val == '[':
            stk.append(val)

        # 닫는 괄호일 경우 두가지를 확인. 1) 이전에 입력 받은 괄호가 있는가  2) 이전에 입력 받은 괄호와 짝이 맞는가
        elif val == ')':
            if not stk:
                print("no")
                result = False
                break
            elif stk[-1] == '(':
                stk.pop()
            else:
                print("no")
                result = False
                break
    
        elif val == ']':
            if not stk:
                print("no")
                result = False
                break
            elif stk[-1] == '[':
                stk.pop()
            else:
                print("no")
                result = False
                break
    
    # 위 조건을 통과한 경우 균형잡힌 문자열이다
    if result:
        print("yes")