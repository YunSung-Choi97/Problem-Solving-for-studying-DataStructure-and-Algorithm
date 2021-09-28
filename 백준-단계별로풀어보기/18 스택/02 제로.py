N = int(input())  # N : 입력받을 정수의 개수
Num_lst = []  # Num_lst : 입력받은 정수를 저장할 리스트. 0을 입력받을 경우 가장 최근의 수를 지움

for i in range(N):  # N번 반복
    num = int(input())  # num : 입력받은 정수를 할당

    # 입력받은 수가 0일 경우
    if not num:
        Num_lst.pop()
    
    # 입력받은 수가 0이 아닐 경우
    else:
        Num_lst.append(num)

print(sum(Num_lst))  # 최종 수의 합계 출력