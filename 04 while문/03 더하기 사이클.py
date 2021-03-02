initial_num = int(input())  # initial_num : 사용자로부터 입력받을 N.

count = 1  # count : 결과로 출력할 사이클 수
while True:  # 무한 반복
    
    # num을 초기화시켜준다
    if count == 1:
        num = initial_num
    else:
        num = new_num
    num10 = num // 10  # num10 : num의 10의 자리 수
    num1 = num % 10  # num1 : num의 1의 자리 수
    new_num = 10 * num1 + (num10 + num1) % 10  # new_num : num으로 만든 새로운 수
    if initial_num == new_num:  # 반복문 종료 조건. 입력받은 수가 새로운 수와 같아질 때
        print(count)
        break
    count += 1  # 사이클 수는 반복문이 수행될때마다 1씩 증가