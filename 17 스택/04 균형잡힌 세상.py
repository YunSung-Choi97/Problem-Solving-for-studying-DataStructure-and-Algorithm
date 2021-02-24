while True:
    data = input()
    if data == '.':
        break
    
    stk = []
    result = True

    for val in data:
    
        if val == '(' or val == '[':
            stk.append(val)
    
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
    if result:
        print("yes")