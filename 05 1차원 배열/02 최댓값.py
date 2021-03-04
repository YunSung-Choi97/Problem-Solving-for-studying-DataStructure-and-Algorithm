num_lst = []  # num_lst : 사용자로부터 입력받은 서로 다른 9개의 자연수를 저장할 리스트

for i in range(9):  # 9번 반복
    num_lst.append(int(input()))  # num_lst에 입력받은 데이터를 정수형으로 바꿔서 추가
max_num = max(num_lst)  # num_lst 중 최댓값을 구함
print(max_num, num_lst.index(max_num)+1, sep = '\n')  # 최댓값과 최댓값의 인덱스를 출력