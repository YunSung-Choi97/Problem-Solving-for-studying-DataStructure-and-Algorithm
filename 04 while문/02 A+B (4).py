while True:  # 무한 반복
    
    # 무한 루프의 종료조건이 문제에 제시되었지 않았기 때문에, 에러가 발생하기 전까지는 프로그램이 동작하도록 해주었다.
    # try, except : 에러가 발생할 경우에 대한 처리
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break