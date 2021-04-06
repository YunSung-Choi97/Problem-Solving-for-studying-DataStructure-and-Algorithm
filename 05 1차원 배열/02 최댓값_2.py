# 1차원 배열을 이용하지 않고 최댓값만 저장해 계산
max_num = 0  # max_num : 입력받은 자연수 중 최댓값을 저장할 변수
for i in range(1, 10):  # 9번 반복. 1 ~ 9번째 자연수 확인
    num = int(input())
    if max_num < num:
        max_num = num
        index = i
print(max_num, index, sep = '\n')