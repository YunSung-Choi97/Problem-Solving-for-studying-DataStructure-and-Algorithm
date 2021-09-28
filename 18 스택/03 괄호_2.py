# 스택 방식이 아닌 문제상황의 조건을 고려하여 코드 작성.

N = int(input())  # N : 입력 데이터 개수

for i in range(N):  # N번 반복
    data = input()  # data : PS/VPS 확인할 입력 데이터
    result = True  # result : data가 PS/VPS인지 판단. PS일 경우 False, VPS일 경우 True


    # 마지막 글자가 ( 가 나오면 안되고, 전체 ( 와 ) 의 개수가 같아야 함.
    if data[-1] == '(' or data.count('(') != data.count(')'):
        print("NO")
        continue

    for idx, val in enumerate(data):  # data의 value를 한 글자씩 읽어와 val에, 그 때의 index를 idx에 할당하여 반복문 수행
        
        # 첫 글자는 ( 가 나와야만 함
        if idx == 0:
            if val != '(':
                print("NO")
                result = False
                break

        # ) 의 다음 글자로 ( 가 나올 경우 ) 의 개수가 더 많으면 안됨
        elif val == '(' and data[idx-1] == ')':
            if data[:idx].count('(') < data[:idx].count(')'):
                print("NO")
                result = False
                break
    
    # 위 3조건을 통과한 경우 VPS이다
    if result:
        print("YES")