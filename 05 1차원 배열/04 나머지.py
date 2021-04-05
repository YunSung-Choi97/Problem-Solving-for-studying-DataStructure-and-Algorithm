R_lst = []  # 입력받은 숫자들을 42로 나눈 나머지를 저장할 리스트

for i in range(10):
    num = int(input())
    R_lst.append(num % 42)

num_set = set(R_lst)  # set형의 순서열에 나머지를 넣어줌으로서 중복된 숫자를 제거

print(len(num_set))