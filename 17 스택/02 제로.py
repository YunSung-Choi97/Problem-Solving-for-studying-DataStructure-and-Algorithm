Num_lst = []  # 입력받은 정수를 저장할 리스트. 0을 입력받을 경우 가장 최근의 수를 지움
N = int(input())  # 입력받을 정수의 개수를 입력받음

for i in range(N):  # N번 수행
    num = int(input())  # 입력받은 정수를 저장

    # 입력받은 수가 0일 경우
    if not num:
        Num_lst.pop()
    
    # 입력받은 수가 0이 아닐 경우
    else:
        Num_lst.append(num)

print(sum(Num_lst))  # 최종 수의 합계 출력