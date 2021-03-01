while True:  # 무한 반복
    
    # try, except : 에러가 발생할 경우에 대한 처리
    try:
        num1, num2 = map(int, input().split())
        print(num1+num2)
    except:
        break