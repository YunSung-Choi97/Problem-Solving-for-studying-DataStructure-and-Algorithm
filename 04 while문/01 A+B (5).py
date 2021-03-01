while True:  # 무한 반복
    A, B = map(int, input().split())  # 
    if A == 0 & B == 0:  # 무한 루프를 빠져나오는 조건
        break
    print(A+B)