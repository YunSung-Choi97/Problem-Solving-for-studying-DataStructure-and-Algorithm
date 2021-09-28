N = int(input())  # N : 입력받을 명령의 개수
lst = []  # lst : push된 정수를 저장하는 스택을 리스트로 구현

for i in range(N):  # N번 반복
    order = input()  # order : 입력받은 명령을 할당

    # push 기능 구현
    if order[:4] == 'push':
        lst.append(int(order[5:]))
    
    # pop 기능 구현
    elif order[:3] == 'pop':
        if not lst:  # 비어있는 리스트는 false를 반환하기 때문에 if not lst 를 통해 빈 리스트 확인
            print(-1)
        else:
            print(lst[-1])
            lst.pop()

    # size 기능 구현
    elif order[:4] == 'size':
        print(len(lst))
    
    # empty 기능 구현
    elif order[:5] == 'empty':
        if not lst:
            print(1)
        else:
            print(0)
    
    # top 기능 구현
    elif order[:4] == 'top':
        if not lst:
            print(-1)
        else:
            print(lst[-1])