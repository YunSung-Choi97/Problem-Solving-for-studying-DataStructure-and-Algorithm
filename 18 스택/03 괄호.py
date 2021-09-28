N = int(input())  # N : 입력 데이터 개수

for i in range(N):  # N번 반복
    data = input()  # data : PS/VPS 확인할 입력 데이터
    result = True  # result : data가 PS/VPS인지 판단. PS일 경우 False, VPS일 경우 True
    stk = []
    
    for val in data:  # data를 한 글자씩 읽어와서 반복문 수행
        
        # ( 글자를 읽을 경우 stk에 추가
        if val =='(':
            stk.append(val)
        
        # ) 글자를 읽을 경우
        # stk이 비었다면 PS이고, 아니라면 하나의 ( 를 제거. 
        else:
            if not stk:
                print("NO")
                result = False
                break
            else:
                stk.pop()
    
    # 모든 데이터를 다 읽고 난 후에 stk안에 남은 괄호가 있다면 VPS가 아님
    if stk:
        print("NO")
        continue
    
    # 위의 조건문과 반복문을 통과한 경우는 모두 VPS이다.
    if result:
        print("YES")